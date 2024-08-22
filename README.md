# PrivacyVideos

PrivacyVideos is a free, open-source, privacy-focused front-end for Xvideos. It is designed to enhance your privacy while accessing adult content, addressing the common concerns associated with mainstream and smaller adult websites.

## Why PrivacyVideos?

Mainstream adult websites like PornHub, YouPorn, RedTube, Xtube, Brazzers, Twistys, MyDirtyHobby, and Reality Kings are notorious for invasive data practices, compromising your privacy. Moreover, adult content is still a sensitive and often taboo topic in many regions. On the other hand, smaller adult sites may seem attractive but often pose significant risks, including the possibility of encountering illegal content or being redirected to suspicious sites.

PrivacyVideos offers a secure and private alternative.

## Key Benefits

- **Privacy-First Approach:** All requests are routed through the backend, ensuring your client never directly interacts with adult websites. This prevents them from tracking your activity or logging your IP address.
- **No JavaScript or Ads:** Enjoy a clean, distraction-free experience with no intrusive scripts or advertisements.
- **Self-Hostable:** You can set up your own private or public instance, giving you complete control over your browsing experience.
- **Enhanced Security:** By using PrivacyVideos, you significantly reduce the risk of exposing personal data or encountering harmful content.

## Getting Started
```sh
git clone https://github.com/CyberDefenseEd/PrivacyVideos
```
### Configure your server
**Set Up Your Configuration**:
   - Copy the provided `config.example.json` to `config.json`.
   - Edit `config.json` to include your server host and port.

The host can be `0.0.0.0` for a public facing host and `127.0.0.1` for local only.
```json
{
  "port": 80,
  "host": "0.0.0.0"
}
```
### Run your server
```sh
cd PrivacyVideos
python server.py
```

