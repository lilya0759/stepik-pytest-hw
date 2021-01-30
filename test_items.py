from selenium import webdriver
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_find_button(browser):
    browser.get(link)
    browser.implicitly_wait(10)
    time.sleep(10)
    result = len(browser.find_elements_by_xpath(
        "//button[@class='btn btn-lg btn-primary btn-add-to-basket']"))
    assert result > 0, "Кнопка не найдена"
