import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver.v2 as uc
import subprocess
import shutil
import time
from pyvirtualdisplay import Display
from selenium import webdriver
from fastapi import FastAPI

# Instantiate the class
app = FastAPI()

@app.get("/anfrage/")
async def send_anfrage(id: str, text: int, user: int):
    display = Display(visible=False, extra_args=[':25'], size=(2560, 1440), backend="xvfb")
    display.start()
    driver = uc.Chrome()
    link = "https://www.immobilienscout24.de/expose/138295962#/basicContact"
    button_id = "button[data-ng-click *= 'submit']"
    text_id = "contactForm-Message"
    salution_id = "contactForm-salutation"
    first_name_id = "contactForm-firstName"
    last_name_id = "contactForm-lastName"
    email_id = "contactForm-emailAddress"
    telefon_id = "contactForm-phoneNumber"
    street_id = "contactForm-street"
    hausnummer_id = "contactForm-houseNumber"
    plz_id = "contactForm-postcode"
    ort_id = "contactForm-city"
    buy_reason_id = "contactForm-buyReason"
    move_in_id = "input[type='radio'][value='FLEXIBLE']"
    persons_id = "contactForm-numberOfPersons"

    employment_id = "contactForm-employmentRelationship"
    income_id = "contactForm-income"
    own_capital_id = "contactForm-ownCapital"
    application_doc_id = "contactForm-applicationPackageCompleted"
    anfrage_button_id = "button[data-ng-click *= 'submit']"
    cookies_button_id = 'button[data-testid="uc-accept-all-button"]'

    # homeOwner

    driver.get(link)
    time.sleep(3)
    try:
        root = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "usercentrics-root")))
        shadow_root = driver.execute_script('return arguments[0].shadowRoot', root)
        time.sleep(3)
        print(shadow_root)
        # time.sleep(6000)
        cookies_button = WebDriverWait(driver, 10).until(
            EC.visibility_of(shadow_root.find_element(by=By.CSS_SELECTOR, value=cookies_button_id)))
        cookies_button.click()
        # uc-center-container > div.sc-bYoBSM.jvautU > div > div > div > button.sc-gsDKAQ.fWOgSr
    except:
        pass

    message = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, text_id)))
    message.send_keys("this is an automated test message")

    salution = Select(WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, salution_id))))
    salution.select_by_value("MALE")

    first_name = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, first_name_id)))
    first_name.send_keys("Esam")

    last_name = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, last_name_id)))
    last_name.send_keys("Hassan")

    email = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, email_id)))
    email.send_keys("esam.hassan@pm-immobilien-gmbh.com")

    telefon = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, telefon_id)))
    telefon.send_keys("017662466206")

    street = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, street_id)))
    street.send_keys("Emil-Geiß-Str.")

    hausnummer = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, hausnummer_id)))
    hausnummer.send_keys("4")

    plz = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, plz_id)))
    plz.send_keys("82031")

    ort = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, ort_id)))
    ort.send_keys("Grünwald")

    time.sleep(15)

    weiter_button = WebDriverWait(driver, 10).until(  # using explicit wait for 10 seconds
        EC.element_to_be_clickable((By.CSS_SELECTOR, button_id))  # finding the element
    )
    weiter_button.click()
    try:
        buy_reason = Select(WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, buy_reason_id))))
        buy_reason.select_by_value("INVESTMENT")
    except:
        pass

    try:
        move_in = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, move_in_id)))
        move_in.click()
    except:
        pass

    try:
        persons = Select(WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, persons_id))))
        persons.select_by_value("TWO_PERSON")
    except:
        pass

    try:
        employment = Select(WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, employment_id))))
        employment.select_by_value("OTHER")
    except:
        pass

    try:
        income = Select(WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, income_id))))
        income.select_by_value("OVER_5000")
    except:
        pass

    try:
        own_capital = Select(WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, own_capital_id))))
        own_capital.select_by_value("OVER_200K")
    except:
        pass

    try:
        application_doc = Select(
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, application_doc_id))))
        application_doc.select_by_value("true")
    except:
        pass

    try:
        anfrage_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, anfrage_button_id)))
        anfrage_button.click()
    except:
        pass

    time.sleep(3)
    driver.quit()
    return
