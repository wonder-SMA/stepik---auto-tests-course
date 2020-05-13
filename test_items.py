from selenium import webdriver
import pytest, time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_button(browser):
    browser.get(link)
    time.sleep(30)
    button = browser.find_element_by_css_selector("button.btn-add-to-basket")
    assert button, "Button not found"