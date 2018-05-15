from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup as bs
import json
import re
import urllib

def login(driver):
	link = "https://something.app.box.com/s/yourlink"
	driver.get(link)

def getToken(driver):
	rawStrJson = re.search('(?<=requestToken\s\=\s\')(.*)(?=\'\;)',rawJsonStr).group(0)


def getFileIds(driver):
	links = {}
	token = "1!aF....//get this from browser"
	l_partlink = "https://dl.boxcloud.com/api/2.0/files/"
	r_partlink = "/content?preview=true&access_token="
	end_partlink = "&shared_link=https%3A%2F%2Fsite.app.box.com%2Fs%2Fsdafadsfasdf&box_client_name=box-content-preview&box_client_version=1.37.1"

	sleep(2)
	print("getting ids")


	soup = bs(driver.page_source, "html.parser")
	rawJsonStr = str(soup.findAll("script")[-1])
	rawTokens = str(soup.findAll("script")[-5])

	rawStrJson = re.search('(?<=shared-folder\"\:)(.*)(?<=viewSize\"\:\d)',rawJsonStr).group(0)
	rawStrJson += "}}"
	convertedJson = json.loads(rawStrJson)


	for item in convertedJson['items']:
		itemID = str(item['id'])
		currentlink = l_partlink + itemID + r_partlink + token + end_partlink
		links[str(item['name'])] = currentlink

	return links


def download(links):
	for link in links.keys():
		print("Downloading {}".format(link))
		print(links[link])
		filename = "/Users/location.../"+link
		urllib.urlretrieve(links[link], filename)

def main():
	driver = webdriver.Firefox(executable_path="drivers/geckodriver")
	login(driver)
	str1 = raw_input("wait till log in...")
	links = getFileIds(driver)
	download(links)

	str3 = raw_input("exit: ")
	driver.exit()

if __name__ == '__main__':
	main()
