import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def test_add_and_delete_todo():
    driver = webdriver.Chrome()

    driver.get("http://localhost:3000")
    time.sleep(2)  # wait for React to load

    input_box = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Enter todo']")
    input_box.send_keys("Learn Selenium")
    add_btn = driver.find_element(By.XPATH,'//*[@id="root"]/div/div/button')
    add_btn.click()

    time.sleep(1)

    # Find todo item using reliable locator
    todo_item = driver.find_element(By.XPATH, "//li[contains(., 'Learn Selenium')]")
    assert todo_item is not None

    # Delete button inside same <li>
    delete_btn = todo_item.find_element(By.TAG_NAME, "button")
    delete_btn.click()

    time.sleep(1)

    # Verify item removed
    items_after_delete = driver.find_elements(By.XPATH, "//li[contains(., 'Learn Selenium')]")
    assert len(items_after_delete) == 0

    driver.quit()
