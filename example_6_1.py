from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Firefox()
driver.get('https://the-internet.herokuapp.com')

driver.find_element_by_link_text('Dropdown').click()

driver.find_element_by_xpath('//*[@id="dropdown"]').click()

options_list = driver.find_elements_by_xpath('//*[@id="dropdown"]/option')
# options_list[0]
# options_list[1].click()
for option in options_list:
    if option.get_attribute('value') == '1':
        option.click()

    if option.text == 'Option 1':
        option.click()


# select = Select()
#
# select.select_by_index(0)
# select.select_by_value('2')
# select.select_by_visible_text('Option 1')
