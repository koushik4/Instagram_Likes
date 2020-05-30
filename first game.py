from selenium import webdriver
import time

class Instagram:
    def __init__(self):
        self.driver=webdriver.Chrome("F:\chromedriver.exe")
        self.driver.get("https://www.instagram.com/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(4)
        #login
        username=self.driver.find_element_by_name("username")
        password=self.driver.find_element_by_name("password")
        login=self.driver.find_element_by_xpath("//*[@id='react-root']/section/main/article/div[2]/div[1]/div/form/div[4]/button/div")
        username.send_keys("(Your username)")
        password.send_keys("(Your Password)")
        login.click()
        self.driver.implicitly_wait(4)
        #not now
        notnow=self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div[3]/button[2]")
        notnow.click()
        #Search
        search = self.driver.find_element_by_xpath("//*[@id='react-root']/section/nav/div[2]/div/div/div[2]/input")
        search.send_keys("(Page to be searched)")
        self.driver.implicitly_wait(3)
        name = self.driver.find_element_by_xpath(
            "//*[@id='react-root']/section/nav/div[2]/div/div/div[2]/div[2]/div[2]/div/a[1]/div/div[2]/div/span")
        name.click()
        self.driver.implicitly_wait(10)
    def Like(self):
        self.driver.implicitly_wait(4)
        pic=self.driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/div[2]/article/div/div")
        pics=pic.find_elements_by_class_name("_9AhH0")
        for p in pics:
            p.click()
            self.driver.implicitly_wait(4)
            like = self.driver.find_element_by_xpath(
                "/html/body/div[4]/div[2]/div/article/div[2]/section[1]/span[1]/button")
            like.click()
            exit = self.driver.find_element_by  _xpath("/html/body/div[4]/div[3]/button")
            time.sleep(2)
            exit.click()
        print(pics)

instagram=Instagram()
instagram.Like()
instagram.driver.quit()