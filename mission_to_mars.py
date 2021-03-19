#!/usr/bin/env python
# coding: utf-8

# ## NASA Mars News

# In[1]:


# import dependencies
import pandas as pd
import requests
import pymongo
from splinter import Browser
from bs4 import BeautifulSoup as bs
from webdriver_manager.chrome import ChromeDriverManager


# #### Scrape the [NASA Mars News Site] (https://mars.nasa.gov/news/) and collect the latest News Title and Paragraph Text. Assign the text to variables that you can reference later.

# In[2]:


# Setup splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[3]:


# add url for NASA's latest news
url = "https://mars.nasa.gov/news/"

# open the url
browser.visit(url)


# In[4]:


# create the html
html = browser.html


# In[5]:


# create the BeautifulSoup object
soup = bs(html, 'html.parser')


# In[6]:


# get the latest news data
data = soup.find("li", class_="slide")
print(data)


# In[7]:


# get the news title and paragraph info
news_title = data.find("div", class_="content_title").a.text
paragraph = data.find("div", class_="article_teaser_body").text
print(news_title)
print("------------")
print(paragraph)


# ## JPL Mars Space Images - Featured Image

# In[8]:


# use splinter to navigate the page
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[9]:


# add url for JPL Featured Space Image
img_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"

# use browser to open the url for the image
browser.visit(img_url)


# In[10]:


# create the html
html = browser.html


# In[11]:


# create the BeautifulSoup object
soup = bs(html, 'html.parser')


# In[12]:


# get the image
image = soup.find("div", class_="SearchResultCard")


# In[13]:


print(image)


# In[14]:


# store image
featured_image_url = 'https://d2pn8kiwq2w21t.cloudfront.net/images/jpegPIA24466.width-1024.jpg'


# In[15]:


print(featured_image_url)


# In[16]:


browser.quit()


# ## Mars Facts

# #### Visit the Mars Facts webpage and use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.

# In[2]:


# add url for Mar's facts
facts_url = "https://space-facts.com/mars/"


# In[4]:


# Use pandas to parse the content from the website
table = pd.read_html(facts_url)
table


# In[5]:


# convert table to pandas dataframe
facts_df = table[0]
facts_df


# In[6]:


#rename the columns
facts_df.columns=["description", "value"]
facts_df


# In[7]:


# reset the index
facts_df.set_index("description", inplace=True)
facts_df


# In[8]:


# convert dataframe to an html table string
facts_html = facts_df.to_html()
print(facts_html)


# In[ ]:


browser.quit()


# ## Mars Hemispheres

# #### Visit the USGS Astrogeology site. Save the image url string for the full resolution hemisphere image, and the title.

# In[11]:


# Setup splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[12]:


# add url for USGS images
url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"

# open the url
browser.visit(url)


# In[13]:


# create the html
html = browser.html


# In[14]:


# create the BeautifulSoup object
soup = bs(html, 'html.parser')


# In[16]:


# get the image
image = soup.find_all("div", class_="item")
print(image)


# In[17]:


# navigate the page to get the image url and title
image = soup.find_all("div", class_="item")

# create empty dataframe to hold the content
hemisphere_img_urls = []


# In[18]:


# loop through image data to find title and url info
for i in image:
    title = i.find("h3").text
    
    img_url = i.a["href"]
    
    url = "https://astrogeology.usgs.gov" + img_url
    
    # use requests to get full images url 
    response = requests.get(url)
    
    # create soup object
    soup = bs(response.text,"html.parser")
    
    # find full image url
    new_url = soup.find("img", class_="wide-image")["src"]
    
    # create full image url
    full_url = "https://astrogeology.usgs.gov" + new_url
    
    # make a dict and append to the list
    hemisphere_img_urls.append({"title": title, "img_url": full_url})

hemisphere_img_urls


# In[ ]:


browser.quit()

