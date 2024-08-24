
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import pandas as pd
import json

url = "https://kaveri.karnataka.gov.in"
PATH = "/Users/sachinsen/Documents/Generative Ai/Claases/SCRAPING/Selenium/chromedriver-mac-arm64/chromedriver"

# Setup WebDriver
driver_path = PATH  # Change this to your ChromeDriver path
driver = webdriver.Chrome(executable_path=driver_path)
driver.get(url)


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

url = "https://kaveri.karnataka.gov.in"
PATH = "/Users/sachinsen/Documents/Generative Ai/Claases/SCRAPING/Selenium/chromedriver-mac-arm64/chromedriver"

# Setup WebDriver
driver_path = PATH  # Change this to your ChromeDriver path
driver = webdriver.Chrome(executable_path=driver_path)
driver.get(url)

District = []
Taluka = []
Hobli = []
Village = []
json_list = []
# District1 = {}
talukas_all = []
district = driver.find_element_by_name("district")
all_option = district.find_elements_by_tag_name("option")
for i in all_option:
    #print(i.text)
    if "Select District"==i.text:
        pass
    else:
        #print(i.text)
        #District.append(i)
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

                            #Create a DataFrame for the current set of data
                            df = pd.DataFrame({
                                'District': [District[-1]],  # Use the most recent entry
                                'Taluka': [Taluka[-1]],      # Use the most recent entry
                                'Hobli': [Hobli[-1]],        # Use the most recent entry
                                'Village': [Village[-1]]     # Use the most recent entry
                            })

                            # Convert DataFrame to JSON (dictionary) and append to the JSON list
                            json_list.append(df.to_dict(orient='records')[0])
            
            # District1={}
            # District1[i.text] = taluka_option.text
            # talukas_all.append(District1)

import pandas as pd
data= talukas_all
# data.to_csv("/Users/sachinsen/Documents/Generative Ai/Claases/SCRAPING/Selenium/test.csv")
print(len(District))
print(len(Taluka))


# Convert the final JSON list to a JSON string if needed
json_string = json.dumps(json_list, indent=4)