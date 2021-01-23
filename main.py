#so why am i doing that? Very simple. I have a few Instagram accounts and if you have those too
#you will know that it is very time consuming sometimes (following and unfollowing people)
#a while ago instagram had a good api that you could use but thats not the case anymore so lets
#use webscraping instead.

from selenium import webdriver
#you can eather way insert one account or multiple accounts the programm will adapt to the number of accounts
usernames = [""]
passwords = [""]

drivers = []
for i in usernames:
    driver = webdriver.Chrome('/opt/homebrew/bin/chromedriver')
    drivers.append(driver)

for i in drivers:
    i.get("https://www.instagram.com/")


