import time
import smtplib
from selenium import webdriver

## Read the list of path to monitored products
pathfile = open('list.txt', 'r')
Lines = pathfile.readlines()
print(Lines)

in_stock = []

#send mail function
def send_mail(url):
  print('sending an email')
  email_login = ""
  email_p = ""
  message = "ITEM IS IN STOCK. LINK: " + url
  s = smtplib.SMTP('smtp.gmail.com', 587)
  s.ehlo()
  s.starttls()
  s.ehlo()
  s.login(email_login, email_p)
  s.sendmail(email_login, 'tnle379@gmail.com', message)
  s.quit()

browser = webdriver.Chrome('chromedriver')

## Visit all the products to monitor stock
for line in Lines:
  url = line.replace('\n','')
  print(url)
  browser.get(url)

  #load a paragraphs of DOM into a list
  all_para = browser.find_elements_by_tag_name("p")
  all_para = [i.text for i in all_para]

  #Check if item is in stock
  if "Out of stock" not in all_para:
    print("Item is out of STOCK")
    if url not in in_stock:
        send_mail(url)
        print("sent an email for this item")

browser.close()
