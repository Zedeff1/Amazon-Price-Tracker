import credentials
from selenium import webdriver

PATH = 'C:/Program Files (x86)/chromedriver.exe'

product_name = input("Enter product name: \n")       #get product name

directory = 'reports'
name = product_name
currency = '₹'
min_price = input("Enter the minimum price that you are looking for: \n")
max_price = input("Enter the maximum price that you are looking for: \n")
FILTERS = {
	'min_price': min_price,
	'max_price': max_price
}
base_url = "http://www.amazon.in/"


def get_chrome_web_driver(options):
	return webdriver.Chrome(PATH, chrome_options=options)

def get_web_driver_options():
	return webdriver.ChromeOptions()

def set_ignore_certificate_error(options):
	options.add_arguments('--ignore-certificate-errors')

def set_browser_as_incognito(options):
	options.add_arguments('--incognito')

def set_automation_as_headless(options):
	options.add_arguments('--headless')

