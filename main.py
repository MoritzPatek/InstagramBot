#so why am i doing that? Very simple. I have a few Instagram accounts and if you have those too
#you will know that it is very time consuming sometimes (following and unfollowing people)
#a while ago instagram had a good api that you could use but thats not the case anymore so lets
#use webscraping instead.
from time import sleep

from selenium import webdriver
#you can eather way insert one account or multiple accounts the programm will adapt to the number of accounts
from selenium.common.exceptions import NoSuchElementException

usernames = [""]
passwords = [""]

drivers = []
for i in usernames:
    driver = webdriver.Chrome('/opt/homebrew/bin/chromedriver')
    drivers.append(driver)

#funtion that checks if elemts exsists
def check_exists_by_xpath(xpath, x):
    try:
        x.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True

#opening browsers
for i in drivers:
    i.get("https://www.instagram.com/")
    sleep(2)
    acceptCookiesBTN = i.find_element_by_xpath("/html/body/div[2]/div/div/div/div[2]/button[1]")
    acceptCookiesBTN.click()


sleep(5)
#login the accounts and pressing all the other neccesary buttons
for i in range(len(drivers)):
    usernameField = drivers[i].find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input")
    passwordField = drivers[i].find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input")
    loginBtn = drivers[i].find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button")
    usernameField.send_keys(usernames[i])
    passwordField.send_keys(passwords[i])
    sleep(1)
    loginBtn.click()
    sleep(5)
    notNowBtn = drivers[i].find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button")
    notNowBtn.click()
    sleep(5)
    notNowBtn = drivers[i].find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]")
    notNowBtn.click()



#now all the bots will get lead to the people that the pages subscribes

for i in range(len(drivers)):
    profilePicture = drivers[i].find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]/span/img")
    profilePicture.click()
    sleep(2)
    profile = drivers[i].find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]/div[2]/div[2]/div[2]/a[1]")
    profile.click()



sleep(5)

#every run the bot unfollows 5 accounts
runs = 2
for i in range(runs):
    sleep(2)
    for x in drivers:
        sleep(2)
        subscribed = x.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[3]/a")
        subscribed.click()
        sleep(5)
        for z in range(5):
            sleep(2)
            unfolowBTN = x.find_element_by_xpath("/html/body/div[5]/div/div/div[2]/ul/div/li["+str(z+1)+"]/div/div[3]/button")
            unfolowBTN.click()
            sleep(2)
            if check_exists_by_xpath("/html/body/div[6]/div/div/div/div[3]/button[1]", x) is True:
                dontFollowAnymoreBTN = x.find_element_by_xpath("/html/body/div[6]/div/div/div/div[3]/button[1]")
                dontFollowAnymoreBTN.click()
    x.refresh()
    sleep(5)


