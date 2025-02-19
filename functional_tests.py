from selenium import webdriver

driver = webdriver.Firefox()
driver.get("http://localhost:8000")

try:
    assert "The install worked successfully! Congratulations!" == driver.title
    print("The install worked successfully! Congratulations!")
except AssertionError:
    print("The install did not work successfully.")
finally:
    driver.quit()