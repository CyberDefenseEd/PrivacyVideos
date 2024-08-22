import requests
from quart import render_template, request
from datetime import datetime
from . import home_bp
from util import fetch_homepage, extract_video_data, FEATURED_VIDEOS
from bs4 import BeautifulSoup

LAST_FEATURED_UPDATED = datetime.now()
TOTAL_PAGES = 1

@home_bp.route('/', methods=['GET'])
async def index():
    search_query = request.args.get('query')
    video_page = int(request.args.get('page', 1))
    videos = []
    total_pages = 1
    
    if search_query:
        search_query = search_query.replace('-', ' ')
        search_url = f'https://www.xvideos.com/?k={search_query}&p={video_page}'
        response = requests.get(search_url)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        videos = extract_video_data(soup)
        
        # Extract pagination
        pagination_section = soup.find('div', class_='pagination')
        if pagination_section:
            pages = pagination_section.find_all('a')
            total_pages = max([int(page.get_text()) for page in pages if page.get_text().isdigit()], default=1)
    
    else:
        videos = FEATURED_VIDEOS

    return await render_template(
        'index.html',
        videos=videos,
        search_query=search_query,
        last_update=LAST_FEATURED_UPDATED.strftime('%Y-%m-%d %H:%M:%S'),
        current_page=video_page,
        total_pages=total_pages
    )
