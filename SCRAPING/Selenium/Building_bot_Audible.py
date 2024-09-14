from selenium import webdriver
import pandas as pd

#website = "https://www.audible.in/adblbestsellers?ref_pageloadid=k17bLLg84tiHiVBs&ref=a_hp_t1_navTop_pl1cg0c1r0&pf_rd_p=4e150d5e-ca98-47fb-823b-f6fcb252aced&pf_rd_r=3GCVFCZHC4XKV5GC55TT&pageLoadId=G0MjCClXV4p7GO1d&creativeId=2e6787a2-0cd0-4a6e-afe0-05766cd505e5"
web = "https://www.audible.in/search"

path = "/Users/sachinsen/Documents/Generative Ai/Claases/SCRAPING/Selenium/chromedriver-mac-arm64/chromedriver"

driver = webdriver.Chrome(executable_path=path)

driver.get(web)
driver.maximize_window()

container = driver.find_element_by_class_name('adbl-impression-container ')
products = container.find_elements_by_xpath("//li[contains(@class,'productListItem')]")

book_title = []
book_author = []
book_length = []
# Looping through the products list (each "product" is an audiobook)
for product in products:
    # We use "contains" to search for web elements that contain a particular text, so we avoid building long XPATH
    book_title.append(product.find_element_by_xpath('.//h3[contains(@class, "bc-heading")]').text)  # Storing data in list
    book_author.append(product.find_element_by_xpath('.//li[contains(@class, "authorLabel")]').text)
    book_length.append(product.find_element_by_xpath('.//li[contains(@class, "runtimeLabel")]').text)

driver.quit()
# Storing the data into a DataFrame and exporting to a csv file
df_books = pd.DataFrame({'title': book_title, 'author': book_author, 'length': book_length})
df_books.to_csv('books.csv', index=False)