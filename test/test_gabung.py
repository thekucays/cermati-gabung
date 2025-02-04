from playwright.sync_api import Page, expect
from pom.POM_gabung import *
from pom.POM_otp import *
from pom.POM_captcha import *
from helper.randomgenerator import *
import time

def test_gabung_cermati(page: Page):
    page.goto("https://www.cermati.com/gabung")

    # landed
    assert page.locator(GABUNG_input_email()).is_visible()

    # fill
    page.fill(GABUNG_input_phone(), generate_phone())
    page.fill(GABUNG_input_email(), generate_random_email())
    page.fill(GABUNG_input_firstname(), "Luki")
    page.fill(GABUNG_input_lastname(), "Ramadon")

    #submit 
    page.click(GABUNG_button_submit())

    # Locate the first reCAPTCHA iframe
    iframe = page.frame_locator(recaptcha_iframe()).first

    # Click the "Saya Bukan Robot" checkbox inside the iframe for recapctha
    iframe.locator(recaptcha_checkbox()).click()