# PrivacyVideos

<img src="https://github.com/CyberDefenseEd/PrivacyVideos/blob/main/assets/example.png?raw=true">

PrivacyVideos is a free, open-source, privacy-focused front-end for X-Videos. It is designed to enhance your privacy while accessing adult content, addressing the common concerns associated with mainstream and smaller adult websites.

## Why PrivacyVideos?

Mainstream adult websites like PornHub, YouPorn, RedTube, Xtube, Brazzers, Twistys, MyDirtyHobby, and Reality Kings are notorious for invasive data practices, compromising your privacy. Moreover, adult content is still a sensitive and often taboo topic in many regions. On the other hand, smaller adult sites may seem attractive but often pose significant risks, including the possibility of encountering illegal content or being redirected to suspicious sites and ads.

PrivacyVideos offers a secure and private alternative.

## Key Benefits

- **Privacy-First Approach:** All requests are routed through the backend, ensuring your client never directly interacts with adult websites. This prevents them from tracking your activity or logging your IP address.
- **No JavaScript or Ads:** Enjoy a clean, distraction-free experience with no intrusive scripts or advertisements.
- **Self-Hostable:** You can set up your own private or public instance, giving you complete control over your browsing experience.
- **HD Always:** Always receive the highest quality video files without ever paying a cent. 
- **Enhanced Security:** By using PrivacyVideos, you significantly reduce the risk of exposing personal data or encountering harmful content.
- **Async By Default:** By using Quart and Hypercorn, we can transform our Python codebase into a production-ready application.

## Getting Started
```sh
git clone https://github.com/CyberDefenseEd/PrivacyVideos
```
### Run your server
Install dependencies 
```
cd PrivacyVideos
pip install -r requirements.txt
```
#### Debug
```sh
python server.py
```
#### Production
```sh
chmod +x ./start-prod.sh
./start-prod.sh
```
