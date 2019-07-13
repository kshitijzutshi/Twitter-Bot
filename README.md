# Twitter-Bot
Tinkering existing twitter bot codes online for some cool features.


# Steps to get started

1. Download the Geckodriver Zip from the following GitHub repo- https://github.com/mozilla/geckodriver/releases
2. Use the pip install command to get the selenium package on your system
3. Unzip the downloaded Geckodriver executable into the python directory
  3.1 For Windows users- C:// Programdata/..local/python/ and paste in the version folder
  3.2 For mac users- paste it in /usr/local/bin [type in spotlight, thats how i went to the location]
4. Follow the code included above with a change, you may get path define error because system is unable to locate the Geko driver, hence include the path in the parameters in webdriver.Firefox()

# NOTE

For this task we are going ahead with automating the user interaction with the twitter web page, hence we go ahead with Selenium.

Those who dont know about selenium, here is what i picked up as definition from google- 

WebDriver is a tool for automating web application testing, and in particular to verify that they work as expected. It aims to provide a friendly API that's easy to explore and understand, easier to use than the Selenium-RC (1.0) API, which will help to make your tests easier to read and maintain. Hence we are using Selenium 2.0 as its primary new feature is integration of the WebDriver API.
