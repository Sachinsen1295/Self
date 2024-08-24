from selenium import webdriver

website = "https://www.audible.in/adblbestsellers?ref_pageloadid=k17bLLg84tiHiVBs&ref=a_hp_t1_navTop_pl1cg0c1r0&pf_rd_p=4e150d5e-ca98-47fb-823b-f6fcb252aced&pf_rd_r=3GCVFCZHC4XKV5GC55TT&pageLoadId=G0MjCClXV4p7GO1d&creativeId=2e6787a2-0cd0-4a6e-afe0-05766cd505e5"


path = "/Users/sachinsen/Documents/Generative Ai/Claases/SCRAPING/Selenium/chromedriver-mac-arm64/chromedriver"

driver = webdriver.Chrome(executable_path=path)

driver.get(website)
driver.maximize_window()

driver.quit()

