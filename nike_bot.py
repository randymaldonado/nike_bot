from selenium import webdriver
from selenium.webdriver import ActionChains
import time
import sys

"""
need to parse HTML for 'option value' and figure out which option
"""

## SHIPPING INFORMATION
my_email = ""
my_first_name = ""
my_late_name = ""
my_address = ""
my_city = ""
my_zipcode = ""
my_phone_number = ""

footwear_page= "https://store.nike.com/us/en_us/pw/mens-jordan-shoes/7puZofqZoi3"
cart_page = "https://secure-store.nike.com/us/checkout/html/cart.jsp?country=US&country=US&l=cart&route=html"
path = "/Users/randymaldonado/Documents/Bots/chromedriver"

driver = webdriver.Chrome(path)

# Select shoe size and add to cart, then click on cart
driver.get(url=footwear_page)

select_size_xpath = '//*[@id="product-variants"]'
size_10_xpath = '//*[@id="product-select"]/option[2]'
add_to_cart_xpath = '//*[@id="product-form-11384363093"]/input'

select_size = driver.find_element_by_xpath(select_size_xpath)
size_10 = driver.find_element_by_xpath(size_10_xpath)
add_to_cart = driver.find_element_by_xpath(add_to_cart_xpath)

select_size.click()
size_10.click()
add_to_cart.click()


# On cart page to proceed to checkout page
driver.get(url=cart_page)

check_out_id = 'checkout'
check_out = driver.find_element_by_id(check_out_id)
check_out.click()

check_out_page_url = driver.current_url

# Filling in form for checkout

driver.get(url=check_out_page_url)

email_xpath = '//*[@id="checkout_email"]'
first_name_xpath = '//*[@id="checkout_shipping_address_first_name"]'
last_name_xpath = '//*[@id="checkout_shipping_address_last_name"]'
address_xpath = '//*[@id="checkout_shipping_address_address1"]'
city_xpath = '//*[@id="checkout_shipping_address_city"]'
zip_code_xpath = '//*[@id="checkout_shipping_address_zip"]'
phone_number_xpath = '//*[@id="checkout_shipping_address_phone"]'
continue_to_shipping_xpath = '//*[@id="content"]/div/div[1]/div[2]/form/div[2]/button'

email = driver.find_element_by_xpath(email_xpath)
email.send_keys(my_email)

first_name = driver.find_element_by_xpath(first_name_xpath)
first_name.send_keys(my_first_name)

last_name = driver.find_element_by_xpath(last_name_xpath)
last_name.send_keys(my_late_name)

address = driver.find_element_by_xpath(address_xpath)
address.send_keys(my_address)

city = driver.find_element_by_xpath(city_xpath)
city.send_keys(my_city)

zip_code = driver.find_element_by_xpath(zip_code_xpath)
zip_code.send_keys(my_zipcode)

phone_number = driver.find_element_by_xpath(phone_number_xpath)
phone_number.send_keys(my_phone_number)


# Timer
for remaining in range(45, 0, -1):
    sys.stdout.write("\r")
    sys.stdout.write("{:2d} seconds remaining.".format(remaining))
    sys.stdout.flush()
    time.sleep(1)

sys.stdout.write("\rComplete!            \n")




continue_to_shipping = driver.find_element_by_xpath(continue_to_shipping_xpath)
continue_to_shipping.click()


select_shipping_url = driver.current_url

# Select Shipping Page
driver.get(select_shipping_url)

continue_to_payment_xpath = '//*[@id="content"]/div/div[1]/div[2]/form/div[2]/button'

continue_to_payment = driver.find_element_by_xpath(continue_to_payment_xpath)
continue_to_payment.click()

payment_page_url = driver.current_url


# Payment page

driver.get(url=payment_page_url)



## BILLING INFORMATION

my_cc_number = ""
my_name_on_card = ""
my_cc_expiry = ""
my_cvv = ""

credit_card_iframe_xpath = "card-fields-number-jawrhqg7pwd00000"
credit_card_xpath = '//*[@id="number"]'


name_on_card_xpath = '//*[@id="payment-gateway-subfields-46701382"]/div[3]/div[2]'
expiry_xpath = '//*[@id="payment-gateway-subfields-46701382"]/div[3]/div[3]'
cvv_xpath = '//*[@id="payment-gateway-subfields-46701382"]/div[3]/div[4]'
complete_order_xpath = '//*[@id="content"]/div/div[1]/div[2]/form/div[2]/button'

driver.switch_to.frame(driver.find_element_by_id(credit_card_iframe_xpath))
credit_card = driver.find_element_by_xpath(credit_card_xpath)
credit_card.click()
credit_card.send_keys(my_cc_number)


# name_on_card = driver.find_element_by_xpath(name_on_card_xpath)
# name_on_card.send_keys(my_name_on_card)
#
# expiry = driver.find_element_by_xpath(expiry_xpath)
# expiry.send_keys(my_cc_expiry)
#
# cvv = driver.find_element_by_xpath(cvv_xpath)
# cvv.send_keys(my_cvv)
#
# complete_order = driver.find_element_by_xpath(complete_order_xpath)
# complete_order.click()

