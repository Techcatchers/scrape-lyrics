import time
from selenium import webdriver
import requests
from bs4 import BeautifulSoup


def lyrics_generator(song_name):
    try:
        # Method 1 Genius.com
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        options.add_argument('window-size=1200x600')

        browser = webdriver.Chrome(
            r'Enter your chromedriver PATH here', chrome_options=options)

        s = "https://www.google.co.in/search?q=" + song_name + "%20genius%20lyrics"
        # s = "https://genius.com/Hailee-steinfeld-and-alesso-let-me-go-lyrics"
        browser.get(s)

        sear = browser.find_element_by_xpath('//*[@class="r"]/a')
        sear = sear.get_attribute("href")

        browser.quit()

        page = requests.get(sear)
        soup = BeautifulSoup(page.content, 'html.parser')
        extract = soup.select(".lyrics")
        lyrics = (extract[0].get_text()).strip()

        return lyrics

    except Exception as e:
        try:
            # Method 2 musixmatch.com
            options = webdriver.ChromeOptions()
            options.add_argument('headless')
            options.add_argument('window-size=1200x600')

            browser = webdriver.Chrome(
                r'C:\Users\Rishabh-Pc\Downloads\chromedriver', chrome_options=options)
            mystr = song_name
            s = "https://www.musixmatch.com/"
            browser.get(s)
            time.sleep(2)

            cookies = browser.find_element_by_xpath(
                '//*[@id="site"]/div/div[2]/div[1]/div[1]/button')
            cookies.click()
            time.sleep(1)

            sbtn = browser.find_element_by_xpath(
                '//*[@id="site"]/div/div[1]/div/main/div/div[1]/div[2]/div/div/div/div[1]/div/span/span/span/form/div/div[1]/input')
            sbtn.send_keys(str(mystr))
            time.sleep(3)

            mysearch = browser.find_element_by_xpath(
                '//*[@id="site"]/div/div[1]/div/main/div/div[1]/div[2]/div/div/div/div[1]/div/span/span/span[2]/div/div/div/div[1]/div[2]/div/ul/li/a/div[2]')
            mysearch.click()
            time.sleep(2)

            ele = browser.find_elements_by_class_name('mxm-lyrics__content ')
            lyrics = ''
            for e in ele:
                lyrics += e.text + "\n"

            browser.quit()

            if lyrics == '':
                lyrics = ["We are not authorised to get the lyrics for this song."]

            return lyrics

        except Exception as e:
            lyrics = ["No Lyrics found for this song."]
            browser.quit()
            return lyrics

# Run this function for testing purposes
# print(lyrics_generator("Let me go"))
