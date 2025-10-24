from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import date
import time

class board_member:
    def __init__(self, fName, lName, email):
        self.fName = fName
        self.lName = lName
        self.email = email

board_members = [board_member("Jason", "Huynh", "jhuynh92@calpoly.edu"), board_member("Phuong", "Nguyen", "pnguy220@calpoly.edu"), board_member("Angel", "Balbuena", "anbalbue@calpoly.edu"), board_member("Carys", "Nguyen", "cnguy405@calpoly.edu")]
num = 13
if date.today().strftime("%A") == "Friday":
    num = 10
for i in range (1, num):
    if i in (1, 2, 3):
        cur_board_member = board_members[0]
    elif i in (4,5, 6):
        cur_board_member = board_members[1]
    elif i in (7, 8, 9):
        cur_board_member = board_members[2]
    else:
        cur_board_member = board_members[3]
    driver = webdriver.Chrome()
    

    driver.get("https://schedule.lib.calpoly.edu/space/211663")
    time.sleep(2)
    next_avail_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="eq-time-grid"]/div[1]/div[1]/button[2]'))
    )
    next_avail_btn.click()
    time.sleep(3)

    booking = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, f'//*[@id="eq-time-grid"]/div[2]/div/table/tbody/tr/td[3]/div/div/div/table/tbody/tr/td/div/div[2]/div[{i}]'))
    )
    booking.click()
    time.sleep(5)

    choose_booking = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="submit_times"]'))
    )
    choose_booking.click()
    time.sleep(5)

    first_Name_input = driver.find_element(By.XPATH, '//*[@id="fname"]')
    first_Name_input.send_keys(cur_board_member.fName)
    time.sleep(2)

    last_Name_input = driver.find_element(By.XPATH, '//*[@id="lname"]')
    last_Name_input.send_keys(cur_board_member.lName)
    time.sleep(2)

    email_input = driver.find_element(By.XPATH, '//*[@id="email"]')
    email_input.send_keys(cur_board_member.email)
    time.sleep(2)

    student_checkbox = driver.find_element(By.XPATH, '//*[@id="s-lc-eq-bform"]/div[4]/fieldset/div/div[1]/label/input')
    student_checkbox.click()
    time.sleep(2)

    submit_booking = driver.find_element(By.XPATH, '//*[@id="btn-form-submit"]')
    submit_booking.click()
    time.sleep(5)
    driver.quit()