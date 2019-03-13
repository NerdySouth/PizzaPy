#order pizza automatically
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

def findStore(driver):
	'''
		function that takes the driver and navigates the inital page and inputs the address
		and moves on to the next page.
	'''

	customer_address = {"Street_Address": "Enter Street Address Here",
						"City": "Enter City Here",
						"State": "Enter State in Two letter format",
						"Zip_Code": "Enter zip code as a number, not a string"}

	street = driver.find_element_by_id("Street")
	street.send_keys(customer_address["Street_Address"])

	city = driver.find_element_by_id("City")
	city.send_keys(customer_address["City"])


	state  = Select(driver.find_element_by_id("Region"))
	state.select_by_visible_text(customer_address["State"])

	zip_code = driver.find_element_by_id("Postal_Code")
	zip_code.send_keys(customer_address["Zip_Code"])


	find_store = driver.find_element_by_xpath('//*[@id="locationSearchForm"]/div/div[4]/button')
	find_store.click()


def order(driver):
	'''
		function that takes the driver object and find trhe pizza, and takes the program to the checkout page
	'''

	#goes to pizza page
	specialty_pizza = driver.get("https://www.dominos.com/en/pages/order/#!/section/Food/category/Pizza/")

	#selects the extravaganzza pizza. Can be changed to another specialty pizza
	pizza_choice = driver.get('https://www.dominos.com/en/pages/order/#!/order/variant/new?code=14SCEXTRAV&qty=1&toppings=X:1/1;1|C:1/1;1.5|H:1/1;1|B:1/1;1|P:1/1;1|S:1/1;1|O:1/1;1|R:1/1;1|M:1/1;1|G:1/1;1')
	time.sleep(1)

	#clicks the checkout button for us
	check_out = driver.find_element_by_xpath('//*[@id="orderSummaryInColumn"]/div[2]/div[1]/a')
	check_out.click()
	time.sleep(1)

	#selects no thanks on promo pop up
	no_thanks = driver.find_element_by_xpath('//*[@id="genericOverlay"]/section/div/div[2]/div/a')
	no_thanks.click()
	time.sleep(1)

	cont_checkout = driver.find_element_by_xpath('//*[@id="js-checkoutColumns"]/aside/a')
	cont_checkout.click()

	#needed a way for the program to stop without the chrome window closing. This is not a proper solution but it works for now.
	time.pause()




def main():
	driver = webdriver.Chrome("/Users/tristennollman/cs41-env/STAMP/chromedriver")
	driver.get("https://www.dominos.com/en/pages/order/#!/locations/search/?type=Delivery")

	#enter the address for delivery to be given a proper store
	findStore(driver)

	# get the pizza and move to checkout page
	order(driver)


	driver.quit()




if __name__ == '__main__':
	main()

