from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
import pandas as pd

# Setup WebDriver
driver_path = '/Users/sachinsen/Documents/Generative Ai/Claases/SCRAPING/Selenium/chromedriver-mac-arm64/chromedriver'
driver = webdriver.Chrome(executable_path=driver_path)

url = 'https://kaveri.karnataka.gov.in/landing-page'
driver.get(url)

district_list = []
taluka_list = []

try:
    wait = WebDriverWait(driver, 30)

    # Wait for the district dropdown to be present and find it
    district_dropdown = wait.until(EC.presence_of_element_located((By.NAME, 'district')))
    all_district_options = district_dropdown.find_elements(By.TAG_NAME, 'option')

    for dist in all_district_options:
        dist_text = dist.text
        
        if dist_text == "Select District":
            continue
        
        print(f"Processing district: {dist_text}")
        
        try:
            dist.click()
            
            # Wait for the taluka dropdown to be visible and updated
            taluka_dropdown = wait.until(EC.presence_of_element_located((By.NAME, 'taluka')))
            taluka_options = taluka_dropdown.find_elements(By.TAG_NAME, 'option')
            
            for taluka in taluka_options:
                taluka_text = taluka.text
                
                if taluka_text == "Select Taluka":
                    continue
                
                district_list.append(dist_text)
                taluka_list.append(taluka_text)
                
                print(f"District: {dist_text}")
                print(f"Taluka: {taluka_text}")

        except StaleElementReferenceException:
            print(f"Stale element reference error for district: {dist_text}")
            # Re-locate the element
            district_dropdown = wait.until(EC.presence_of_element_located((By.NAME, 'district')))
            all_district_options = district_dropdown.find_elements(By.TAG_NAME, 'option')

finally:
    
    driver.quit()


data = pd.DataFrame({"District":district_list})
print(data)
