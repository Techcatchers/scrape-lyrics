# Web scraping lyrics with Genius and Musixmatch
Get lyrics of a song by just passing in the song name. There are 2 methods used to find the lyrics for a song so if 1 method fails to find the lyrics for the song then another method comes to the rescue and finds it and returns in a well-formatted lyrics ready for educational use. But if both the method fails than it returns 'No lyrics found for the song.'

We are using selenium with Python 3 in this project. We can also use Google custom search API to get faster results but there are some issues with finding the accurate results for songs on Musixmatch as some of the songs I searched returned 'We are not authorized to get the lyrics for this song.' So I implemented a way to directly search on the website and click the first result to get the best result out of all displayed results. I scrape from genius using Google search query and clicking on the first Genius.com result on Google search so I get the most accurate results even for misspelled song names. 

### Requirements:
* Python installed on your machine
* Selenium Library installed
* ChromeDriver or Firefox installed for browser Automation

<br>

### Copyright Information:
I have uploaded this project for educational use only. Any commercial use of the scraped content may be prohibited by these sites so please read their terms and policies before using them anywhere other than educational uses as Web Scraping may not be allowed by Genius.com and Musixmatch.com. I shall not be liable for any misuse of this project as I have mentioned everything clearly and if you have any doubts about the scraped content usage, please contact the respective site owners.  

#### You are All set to fork this Repository and modify it as per your needs.

#### And Yes, if you like this Repository, then please star this repository as it motivates me to upload more Open Source projects like this.

#### Get Set GO!
