import requests
from selenium import webdriver
import logging as logger
from time import sleep

def main():
  logger.basicConfig(filename='candidatelabs.log',level=logger.INFO)
  driver = webdriver.Safari()
  visited_links = {}
  all_pass = True
  first = True
  driver.get("https://www.candidatelabs.com/jobs")
  print("Sleeping 5 seconds for page to complete loading")
  sleep(5)

  while True:
    if not first:
      driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
      #print("Sleeping 5 seconds for page to complete scrolling")
      sleep(5)
    list_links = driver.find_elements_by_tag_name('a')
    new_link_found = False

    for link in list_links:
      href_link = link.get_attribute('href')
      if href_link not in visited_links and "candidatelabs.com" not in href_link:
          resp = requests.get(href_link)
          if resp.status_code != 200:
            logger.error(f"{href_link} is broken returns status code:{resp.status_code}")
            all_pass = False
            visited_links[href_link] = "FAIL"
          else:
            logger.info(f"{href_link} is working")
            visited_links[href_link] = "PASS"
          print(f"{href_link}:{visited_links[href_link]}")
          print("=========================================")
          new_link_found = True
    if not new_link_found:
      break
    first = False


  result = "PASS" if all_pass else "FAIL"
  logger.info(f"Result: {result}")
  logger.info(f"{visited_links}")


if __name__ == '__main__':
  main()
        
      

