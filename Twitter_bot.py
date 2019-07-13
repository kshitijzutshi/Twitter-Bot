from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class TwitterBot:

    def __init__(self,username,password):

        self.username=username
        self.password=password
        driver=webdriver.Firefox(executable_path = '/usr/local/bin/geckodriver')
        self.bot=driver

    
    def login(self):
        bot=self.bot
        bot.get('http://twitter.com')
        time.sleep(3)
        email=bot.find_element_by_class_name('email-input')
        password=bot.find_element_by_name('session[password]')
        email.clear()
        password.clear()
        email.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(3)

    def like_tweets(self,hashtag):
        bot=self.bot
        #'https://twitter.com/search?q'+hashtag+'&src=typd')
        bot.get('https://twitter.com/search?q'+hashtag+'&src=typd')  
        time.sleep(3)
        search1=bot.find_element_by_id('search-home-input')
        search1.send_keys(hashtag)
        search1.send_keys(Keys.RETURN)
        time.sleep(3)
        for i in range(1,3):
            # scroll to more tweets
            bot.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            time.sleep(2)
            #find the tweet and open it
            tweets=bot.find_elements_by_class_name('tweet')
            #each opened tweet has url when opened
            links=[elem.get_attribute('data-permalink-path') for elem in tweets]

            for link in links:
                bot.get('http://twitter.com'+link)
                try:
                    bot.find_element_by_class_name('user-actions btn-group not-following not-muting').click()
                    bot.find_element_by_class_name('HeartAnimation').click()
                    
                    time.sleep(10)
                except Exception as ex:
                    time.sleep(60)
ed=TwitterBot('SudeepS49693107','kshitij17')
ed.login()
ed.like_tweets('gaming')

#user-actions-follow-button js-follow-btn follow-button



