import requests
from bs4 import BeautifulSoup
import datetime
import re

LAST_FEATURED_UPDATED = datetime.datetime.now()
FEATURED_VIDEOS = []

def fetch_homepage():
    global LAST_FEATURED_UPDATED, FEATURED_VIDEOS
    
    homepage_url = 'https://www.xvideos.com'
    response = requests.get(homepage_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    videos = []
    
    # Extract videos
    for video in soup.find_all('div', class_='thumb-block'):
        link = 'https://www.xvideos.com' + video.find('a')['href']
        thumbnail = video.find('img')['data-src']
        title = video.find('p', class_='title').get_text(strip=True)
        duration = video.find('span', class_='duration').get_text(strip=True)
        author = video.find('span', class_='name').get_text(strip=True)
        views = video.find('span', class_='bg').get_text(strip=True).split('-')[1].strip().split('Views')[0]

        video_data = {
            'link': link,
            'thumbnail': thumbnail,
            'title': title,
            'duration': duration,
            'author': author,
            'views': views
        }

        videos.append(video_data)
        FEATURED_VIDEOS.append(video_data)
        
    # Extract pagination
    pagination_section = soup.find('div', class_='pagination')
    total_pages = 1
    if pagination_section:
        pages = pagination_section.find_all('a')
        total_pages = max([int(page.get_text()) for page in pages if page.get_text().isdigit()], default=1)

    return videos, total_pages

def extract_video_data(soup):
    videos = []
    for video in soup.find_all('div', class_='thumb-block'):
        link = 'https://www.xvideos.com' + video.find('a')['href']
        thumbnail = video.find('img')['data-src']
        title = video.find('p', class_='title').get_text(strip=True)
        duration = video.find('span', class_='duration').get_text(strip=True)
        try:
            author = video.find('span', class_='name').get_text(strip=True)
        except:
            author = 'Anonymous'
        try:
            views = video.find('span', class_='bg').get_text(strip=True).split('-')[1].strip().split('Views')[0]
            if len(views) < 1:
                views = 0
        except:
            views = 0

        video_data = {
            'link': link,
            'thumbnail': thumbnail,
            'title': title,
            'duration': duration,
            'author': author,
            'views': views
        }

        videos.append(video_data)

    return videos

def extract_video_url(content):
    video_url_pattern = re.compile(r"html5player\.setVideoUrlHigh\(['\"](.*?)['\"]\)")
    video_url_match = video_url_pattern.search(content)
    return video_url_match.group(1) if video_url_match else 'URL not found'

def extract_video_details(soup):
    thumbnail_meta = soup.find('meta', property='og:image')
    title_meta = soup.find('meta', property='og:title')
    
    thumbnail = thumbnail_meta['content'] if thumbnail_meta else 'Thumbnail not found'
    title = title_meta['content'] if title_meta else 'Title not found'
    
    tags_section = soup.find('div', class_='video-tags-list')
    tags = []
    if tags_section:
        for tag in tags_section.find_all('a', class_='is-keyword'):
            tag_name = tag.text.strip()
            tag_link = tag['href']
            tags.append({'name': tag_name, 'link': tag_link})
    
    return thumbnail, title, tags
