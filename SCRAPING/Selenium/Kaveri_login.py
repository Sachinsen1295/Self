from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd
import pandas as pd
import json


url = "https://kaveri.karnataka.gov.in"
PATH = "/Users/sachinsen/Documents/Generative Ai/Claases/SCRAPING/Selenium/chromedriver-mac-arm64/chromedriver"


# Setup WebDriver
driver_path = PATH  # Change this to your ChromeDriver path
driver = webdriver.Chrome(executable_path=driver_path)
driver.get(url)

# Set implicit wait
driver.implicitly_wait(10) 

time.sleep(2)
login = driver.find_element_by_xpath("//button[text()='Login']")
login.click()

# Set implicit wait
driver.implicitly_wait(10) 

user_name = driver.find_element_by_id("userName")
user_name.clear()
user_name.send_keys("sachin.sen@propequity.in")


password = driver.find_element_by_id("password")
password.clear()
password.send_keys("Sachin@9899")


Capta = driver.find_element_by_id("loginCaptchaUserInput1")
Capta.clear()
Capta.send_keys(input())

login_button = driver.find_element_by_xpath("//button[text()='Log In']")
login_button.click()


# Set implicit wait
driver.implicitly_wait(10) 

otp = driver.find_element_by_id("otp")
# otp.clear()
otp.send_keys(input())

# Set implicit wait
driver.implicitly_wait(10) 

login_button = driver.find_element_by_xpath("//button[contains(@class, 'btn-primary') and contains(text(), 'Login')]")
login_button.click()

# Set implicit wait
driver.implicitly_wait(10) 

new_application = driver.find_element_by_xpath("//button[contains(@class, 'mat-tooltip-trigger') and contains(@class, 'button')]//a[text()='Start a New Application ']")
new_application.click()

# Set implicit wait
driver.implicitly_wait(10) 

EC = driver.find_element_by_xpath("//div[contains(@class, 'text-center') and contains(@class, 'hovering') and .//span[text()='ENCUMBERANCE CERTIFICATE -(ONLINE EC)']]")
EC.click()

# Set implicit wait
driver.implicitly_wait(10) 

continue_page = driver.find_element_by_xpath("//button[span[text()='Continue'] and contains(@class, 'mat-button') and contains(@class, 'mat-focus-indicator')]")
continue_page.click()

# Set implicit wait
driver.implicitly_wait(10) 

proceed = driver.find_element_by_xpath("//button[text()='Proceed']")
proceed.click()

# Set implicit wait
driver.implicitly_wait(10) 

# Initialize an empty list to store DataFrames
json_list = []

District = []
Taluka = []
Hobli = []
Village = []
# District1 = {}
talukas_all = []
district = driver.find_element_by_name("district")
all_option = district.find_elements_by_tag_name("option")
for i in all_option:
    #print(i.text)
    # if "Select District"==i.text:
    #     pass
    # else:
    #     #print(i.text)
    #     #District.append(i)
    i.click()
    time.sleep(2)
    taluka = driver.find_element_by_name("taluka")
    taluka_options = taluka.find_elements_by_tag_name("option")

    for taluka_option in taluka_options:
            # District.append(i.text)
            # Taluka.append(taluka_option.text)
            taluka_option.click()


            time.sleep(2)
            hobli = driver.find_element_by_name("hobli")
            hobli_options = hobli.find_elements_by_tag_name("option")
            # hobli.click()

            for hobli_option in hobli_options:
                    # District.append(i.text)
                    # Taluka.append(taluka_option.text)
                    # Hobli.append(hobli_option.text)
                    hobli_option.click()

                    time.sleep(2)
                    village = driver.find_element_by_name("village")
                    village_options = village.find_elements_by_tag_name("option")
      

                    for village_option in village_options:
                            District.append(i.text)
                            Taluka.append(taluka_option.text)
                            Hobli.append(hobli_option.text)
                            Village.append(village_option.text)

                            # Create a DataFrame for the current set of data
                            df = pd.DataFrame({
                                'District': [District[-1]],  # Use the most recent entry
                                'Taluka': [Taluka[-1]],      # Use the most recent entry
                                'Hobli': [Hobli[-1]],        # Use the most recent entry
                                'Village': [Village[-1]]     # Use the most recent entry
                            })

                            # Convert DataFrame to JSON (dictionary) and append to the JSON list
                            json_list.append(df.to_dict(orient='records')[0])


driver.quit()

                            

            
            # District1={}
            # District1[i.text] = taluka_option.text
            # talukas_all.append(District1)

import pandas as pd
data= talukas_all
# data.to_csv("/Users/sachinsen/Documents/Generative Ai/Claases/SCRAPING/Selenium/test.csv")
print(len(District))
print(len(Taluka))
print(len(Hobli))
print(len(Village))


# Convert the final JSON list to a JSON string if needed
json_string = json.dumps(json_list, indent=4)

data2=pd.DataFrame({"District":District, "Town":Taluka, "Hobli":Hobli,"Village":Village})
data2.to_csv("/Users/sachinsen/Documents/Generative Ai/Claases/SCRAPING/Selenium/test2.csv")

file_path = "/Users/sachinsen/Documents/Generative Ai/Claases/SCRAPING/Selenium"
# Write the JSON string to a file
with open(file_path, 'w') as file:
    file.write(json_string)

print(f"JSON data successfully saved to {file_path}")