from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from time import sleep


class insta:
    # locators
    site_title = "//h2[1]"
    followers = "(//div[3]//button//span[@class ='_ac2a'])[2][@title]"
    following = "(//div[3]//button//span[@class ='_ac2a'])[3]"

    # method to initialize url and driver

    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

    # method to access web page
    def webpageAccess(self):
        try:
            self.driver.maximize_window()
            self.driver.get(self.url)
            print(self.driver.title)
            sleep(5)
        except:
            print("Error accessing the web page")

    # method to find followers
    def findFollowers(self):
        try:
            siteTitleElement = self.driver.find_element(by=By.XPATH, value=self.site_title)
            site_text = siteTitleElement.text
            followers_element = self.driver.find_element(by=By.XPATH, value=self.followers)
            # this followers data is rendered in attribute called "title", so using get_attribute to get that value
            followers_text = followers_element.get_attribute("title")
            print(f"No. of followers present in {site_text} is {followers_text}")
        except:
            print("Error accessing followers element")

    # method to find following
    def findFollowing(self):
        try:
            siteTitleElement = self.driver.find_element(by=By.XPATH, value=self.site_title)
            site_text = siteTitleElement.text
            following_element = self.driver.find_element(by=By.XPATH, value=self.following)
            # following element is not having any attribute and the data is displayed as text, so text is displayed
            following_text = following_element.text
            print(f"Number of following in {site_text} is {following_text}")
        except:
            print("Error accessing following element")

    def shutdown(self):
        try:
            self.driver.quit()
        except:
            print("Error quitting driver")


url = "https://www.instagram.com/guviofficial/"
vIn = insta(url)
vIn.webpageAccess()
vIn.findFollowers()
vIn.findFollowing()
vIn.shutdown()
