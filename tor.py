import os
import requests
os.system("start C:\\Users\\ammin\\Desktop\\tor.lnk")
proxies = {"http": "socks5://127.0.0.1:9050",
           "https" : "socks5://127.0.0.1:9050"
           }
requests.get("http://example.org", proxies=proxies)