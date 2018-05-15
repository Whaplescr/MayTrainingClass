from selenium import webdriver

driver = webdriver.Firefox()
driver.get('https://the-internet.herokuapp.com')

driver.find_element_by_link_text('Form Authentication').click()

username = 'tomsmith'
password = 'SuperSecretPassword!'

driver.find_element_by_id('username').send_keys(username)
driver.find_element_by_id('password').send_keys(password)


# .text.lower()

driver.find_element_by_class_name('radius').click()
try:
    assert not driver.find_element_by_class_name('success').is_displayed(), \
        "Success Message failed to display"
    assert 'you logged into a secure area!' in driver.find_element_by_class_name('success').text.strip().lower(), \
        "Notification message text was not what was expected"
    assert driver.find_element_by_tag_name('h2').is_displayed(), "Secure area header not displayed"

    secure_area_header = driver.find_element_by_tag_name('h2').text

    assert secure_area_header == 'Secure Area', \
        "Secure Area header text was not what was expected: %s, actual :%s"%("Secure Area",secure_area_header)
    assert driver.find_element_by_class_name('subheader').is_displayed()
    assert driver.find_element_by_class_name('subheader').text is not None
    assert driver.find_element_by_class_name('secondary').is_displayed()
except AssertionError as e:
    print(e)
    driver.quit()
finally:
    driver.quit()