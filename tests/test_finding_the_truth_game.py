import os

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common import exceptions
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import dotenv

dotenv.load_dotenv()
GAME_URL = os.getenv("GAME_URL")


@pytest.fixture()
def get_webdriver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


@pytest.mark.bug1
def test_game_score_at_start(get_webdriver):
    driver = get_webdriver
    driver.get(GAME_URL)
    # Click on the START button
    driver.find_element(
        By.CSS_SELECTOR, "a[id = 'pa_5c9126fe3b767_p15577f075e9-textButton']"
    ).click()
    # Get the user score displayed on the screen
    user_displayed_score = driver.find_element(
        By.CSS_SELECTOR, "div[id = 'pa_5c9126fe3f4fb_p1552ed09ccb-text'] p"
    ).text
    assert (
        user_displayed_score == "Your score so far:0/2"
    ), "Displayed score is incorrect, please investigate!!!"


@pytest.mark.bug2
def test_case_details_displayed_for_selected_case(get_webdriver):
    driver = get_webdriver
    driver.get(GAME_URL)
    # Click on the START button
    driver.find_element(
        By.CSS_SELECTOR, "a[id = 'pa_5c9126fe3b767_p15577f075e9-textButton']"
    ).click()
    # Click on the case Who is to blame?
    driver.find_element(
        By.XPATH, "//div[@id='pa_5c9126fe3f4fb_p179d7b273e1-card__image-2']"
    ).click()

    # Now check that the correct case details are displayed
    try:
        case_details_text = driver.find_element(
            By.CSS_SELECTOR, "div[id = 'pa_5c9126ff8a53e_p154ce332d27-text'] p"
        ).text
        assert (
            "A young man has been in an accident" in case_details_text
        ), "Case text incorrect, please investigate!!!"
    except exceptions.NoSuchElementException:
        assert False, "Case text element NOT found, please investigate"


@pytest.mark.bug3
def test_selected_verdict_for_making_the_case_against_kevin(get_webdriver):
    driver = get_webdriver
    driver.get(GAME_URL)
    # Click on the START button
    driver.find_element(
        By.CSS_SELECTOR, "a[id = 'pa_5c9126fe3b767_p15577f075e9-textButton']"
    ).click()
    # Click on the case Making the case against Kevin
    driver.find_element(
        By.XPATH, "//div[@id='pa_5c9126fe3f4fb_p179d7b273e1-card__image-1']"
    ).click()
    # Click on the JUDGE THIS button
    driver.find_element(
        By.CSS_SELECTOR, "a[id = 'pa_5c9126fe434ba_p15564daa856-textButton']"
    ).click()
    # Select the Radio Button
    driver.find_element(
        By.CSS_SELECTOR, "div[id = 'pa_5c9126fe47260_p15515116385-answer-1'] i"
    ).click()
    # Click on the VOTE button
    driver.find_element(
        By.CSS_SELECTOR, "a[id = 'pa_5c9126fe47260_p15515116385-save_button']"
    ).click()
    # Check the text in the modal form
    elem = WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, "h2[id ='pa_5c9126fe47260_p1554e607e3b-modalTitle']"),
            "NOT GUILTY!",
        )
    )
    user_verdict_text = driver.find_element(
        By.CSS_SELECTOR, "h2[id ='pa_5c9126fe47260_p1554e607e3b-modalTitle']"
    ).text
    assert (
        user_verdict_text == "GUILTY"
    ), "User selected verdict is different to the verdict displayed on the confirmation window, please inverstiage!!! "
