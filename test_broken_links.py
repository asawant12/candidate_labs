import requests
from selenium import webdriver

driver = webdriver.Safari()
visited_links = {}
while True:
  driver.get("https://www.candidatelabs.com/jobs")
  list_links = driver.find_elements_by_tag_name('a')
  new_link_found = False
  for link in list_links:
    href_link = link.get_attribute('href')
    if href_link not in visited_links:
        visited_links[href_link] = 1
        resp = requests.get(href_link)
        if resp.status_code != 200:
          logger.error(f"{href_link} is broken returns status code:{resp.status_code}")
        new_link_found = True
  if not new_link_found:
    break
        
      

