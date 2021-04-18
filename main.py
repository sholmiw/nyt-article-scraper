from bs4 import BeautifulSoup
import requests
from datetime import date
import sys


def get_url(args):
  url = ''.join(args)
  return url

def scrape_url(url):
  html = requests.get(url).text
  soup = BeautifulSoup(html,'lxml') #can use  'html.parser' also
  return soup

def get_title(soup):
  title_text = soup.title.get_text()
  #print("Title: " , title_text)  # fine
  return title_text

def get_text(soup):
  paragraph = soup.find_all('p')
  for i in paragraph:
    print(i.get_text())
  return paragraph

def get_time(soup):
  time_of_pub =  soup.find('time')
  timestring = str(time_of_pub)
  start = timestring.find("datetime=") + 10
  # time format 2021/mm/dd -10 chars.
  time_of_pub = timestring[start:start+10]
  #print(time_of_pub)
  return time_of_pub



def write_news_to_file(title_text,news):
    filename = "News_" + str(date.today()) + ".txt"    
    openF = open(filename, "w+")
    openF.write("*---------------*\n")
    openF.write("Title: \n")
    openF.write(title_text)
    openF.write("\n*---------------*\n")
    openF.writelines(str(date.today()))
    openF.write("\n----------------\n\n\n")
    openF.write("Title: ")
    openF.write(title_text)
    openF.write("\n")
    for i in news:
        openF.write(i.get_text())
        openF.write("\n")

def save(title,ar_time,txt):
  write_in_txt = str(input("Do you want to save the article in .txt ? (Yes or No) : "))
  filename = "News_" + str(date.today()) + ".txt"

  if write_in_txt.upper() == 'yes'.upper():
    write_news_to_file(title,txt)
    print("the article has been saved in", filename)
  else:
    print("the article hasn't been saved")  



def run():
  url = get_url(sys.argv[1:]) 
  # to add cheak url(url)?
  soup = scrape_url(url)
  #title of article from webpage
  title = get_title(soup)
  #time of publaction
  ar_time = get_time(soup)
  # article 
  txt = get_text(soup)
  #print(txt)
  # save article?
  save(title,ar_time,txt)
  print('')





if __name__ == "__main__":
  run()
