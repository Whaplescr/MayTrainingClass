from selenium import webdriver

from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Firefox()

driver.get('https://the-internet.herokuapp.com')

driver.find_element_by_link_text('Dynamic Loading').click()

driver.find_element_by_xpath('//*[@id="content"]/div/a[1]').click()

driver.find_element_by_tag_name('button').click()

# //*[@id="finish"]'
finished = (By.XPATH,'//*[@id="finish"]')

wait = WebDriverWait(driver, 60)

wait.until(EC.visibility_of_all_elements_located(finished))

try:
    assert driver.find_element(finished[0],finished[1]).is_displayed(), "Finished message was not displayed"
except AssertionError as e:
    print(e)
except:
    pass
finally:
    driver.quit()