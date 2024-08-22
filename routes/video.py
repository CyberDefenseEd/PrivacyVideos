import requests
from bs4 import BeautifulSoup
from quart import render_template
from . import video_bp
from util import extract_video_url, extract_video_details

@video_bp.route('/video/<video_id>/<title>') # Searched Videos Endpoint
@video_bp.route('/video/<video_id>/<uid>/<id>/<title>') # Regular Endpoint
async def video_page(video_id, title, uid=None, id=None):
    video_url = f'https://www.xvideos.com/{video_id}/{title}'
    response = requests.get(video_url)
    content = response.text
    
    video_url = extract_video_url(content)
    
    soup = BeautifulSoup(content, 'html.parser')
    thumbnail, title, tags = extract_video_details(soup)
    
    video_data = {
        'url': video_url,
        'thumbnail': thumbnail,
        'title': title,
        'tags': tags
    }
    
    return await render_template('video.html', video=video_data)
