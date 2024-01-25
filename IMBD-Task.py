
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
import time

edge_driver_path = r"C:\Users\a250580\OneDrive - Syneos Health\Documents\Drivers\edgedriver_win64 (3)\msedgedriver.exe"

        # Use Edge class directly and set the executable path using EdgeService
service = webdriver.EdgeService(executable_path=edge_driver_path)
driver = webdriver.Edge(service=service)





# Open the URL
driver.get("https://www.imdb.com/search/name/")
driver.maximize_window()
driver.implicitly_wait(20)
time.sleep(5)


try:
    driver.execute_script("window.scrollTo(0,800);")
    # expand_all_xpath = "//*[@id='__next']/main/div[2]/div[3]/section/section/div/section/section/div[2]/div/section/div[2]/div[1]/div/button/span"
    # expand_all = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, expand_all_xpath)))
    # expand_all.click()
    # Scroll to a certain position
    time.sleep(2)

    # Click on the Name accordion
    name_accordion = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//label[@for='accordion-item-nameTextAccordion']//span[@class='ipc-accordion__item__chevron']//*[name()='svg']")))
    name_accordion.click()

    # Enter name
    name_input = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.NAME, "name-text-input")))
    name_input.send_keys("Pavi")

    # Click on the Birth Date accordion
    birth_accordion = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//label[@for='accordion-item-birthDateAccordion']//span[@class='ipc-accordion__item__chevron']//*[name()='svg']")))
    birth_accordion.click()

    # Enter birth date
    birth_start_input = driver.find_element(By.NAME, "birth-date-start-input")
    birth_start_input.send_keys("01/03/2000")
    birth_end_input = driver.find_element(By.NAME, "birth-date-end-input")
    birth_end_input.send_keys("17/01/2024")

    # Click on the Birthday accordion
    birthday_accordion = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//label[@for='accordion-item-birthdayAccordion']")))
    birthday_accordion.click()
    time.sleep(2)

    # Enter birthday
    birthday_input = driver.find_element(By.NAME, "birthday-input")
    birthday_input.click()

    birthday_input.send_keys("01-02")

    # Click on the Awards accordion
    awards_accordion = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//label[@for='accordion-item-awardsAccordion']//span[@class='ipc-accordion__item__chevron']//*[name()='svg']")))
    awards_accordion.click()


    # Click on the button within the Awards section
    awards_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='accordion-item-awardsAccordion']/div/section/button[4]")))
    awards_button.click()
    time.sleep(2)
# Scroll to the Page Topics accordion
    # Scroll to the Page Topics accordion
    page_topics_accordion = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//label[@for='accordion-item-pageTopicsAccordion']")))
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", page_topics_accordion)

# Wait for the accordion to be clickable
    page_topics_accordion = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//label[@for='accordion-item-pageTopicsAccordion']")))
# Click on the Page Topics accordion using JavaScript
    driver.execute_script("arguments[0].click();", page_topics_accordion)

# Introduce a small delay (you can adjust the timing as needed)
    time.sleep(2)

# Scroll a bit more to ensure the dropdown is fully visible
    driver.execute_script("window.scrollBy(0, 50);")

# Wait for the dropdown to be clickable
    page_topics_dropdown = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "within-topic-dropdown")))

# Select "Quotes" from the dropdown using Selenium Select
    search = Select(page_topics_dropdown)
    search.select_by_visible_text("Quotes")
    time.sleep(2)
#
# #     # Wait for the input field to be present
#     input_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@id='text-input__4298']")))
#
# # Send keys to the input field
#     input_field.send_keys("Arrested")

    # driver.execute_script("window.scrollTo(0,800);")
    #
    # # Click on the Death Date accordion
    # death_date_accordion = WebDriverWait(driver, 20).until(
    #     EC.visibility_of_element_located((By.NAME, "death-date-start-input"))
    # )
    # driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", death_date_accordion)
    #
    # time.sleep(2)  # Introduce a delay after scrolling
    # death_date_accordion.click()
    #
    # # Enter death date range
    # death_date_from_input = WebDriverWait(driver, 20).until(
    #     EC.element_to_be_clickable((By.XPATH, "//*[@id='text-input__864']"))
    # )
    # death_date_to_input = WebDriverWait(driver, 20).until(
    #     EC.element_to_be_clickable((By.XPATH, "//*[@id='text-input__865']"))
    # )
    #
    # # Clear any existing values in the input fields
    # death_date_from_input.clear()
    # death_date_to_input.clear()
    #
    # death_date_from_input.send_keys("02/01/2050")
    # death_date_to_input.send_keys("05/07/2050")

    # GENDER IDENTITY
    gender_accordion = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//label[@for='accordion-item-genderIdentityAccordion']//span[@class='ipc-accordion__item__chevron']//*[name()='svg']")))
    gender_accordion.click()
    time.sleep(2)  # Introduce a small delay before the next interaction

    # Select gender identity
    gender_select = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//div[@id='genderIdentityAccordion']//button[2]")))
    gender_select.click()
    time.sleep(2)

    # CREDITS
#     # Click on the Credits accordion
#     credits_accordion = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.XPATH, "//label[@for='accordion-item-filmographyAccordion']//span[@class='ipc-accordion__item__chevron']//*[name()='svg']"))
# )
#     credits_accordion.click()
#
# # Wait for the input field to be clickable
#     credits_input = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.XPATH, "//input[@type='text']"))
# )
#
# # Click on the input field
#     credits_input.click()
#
# # Send keys to the input field
#     credits_input.send_keys("good")

    #adult

    # Click on the Adult Names accordion
    adult_accordion = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//div[@id='adultNamesAccordion']")))
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", adult_accordion)
    adult_accordion.click()
    time.sleep(2)  # Introduce a small delay before the next interaction

# Select gender identity
    adult_select = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//input[@id='include-adult-names']")))
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", adult_select)
    adult_select.click()

# Check if the checkbox is selected
    if adult_select.is_selected():
     print("Checkbox is selected.")
    else:
      print("Checkbox is not selected.")

except Exception as E:
    print(E)
finally:
    time.sleep(10)
    driver.quit()
