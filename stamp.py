#order pizza automatically
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

def findStore(driver):

	customer_address = {"Street_Address": "658 Escondido rd",
						"City": "Stanford",
						"State": "CA",
						"Zip_Code": 94305}

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

	#must supply your own dominos login here
	customer_info = {"Email": "yudidntcatchit@gmail.com",
					 "Password": "107469TSN"}

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
	time.pause()




def main():
	driver = webdriver.Chrome("/Users/tristennollman/cs41-env/STAMP/chromedriver")
	driver.get("https://www.dominos.com/en/pages/order/#!/locations/search/?type=Delivery")

	#enter the address for delivery to be given a proper store
	findStore(driver)

	order(driver)


	driver.quit()




if __name__ == '__main__':
	main()

