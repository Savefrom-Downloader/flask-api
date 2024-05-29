# Using flask to make an api
# import necessary libraries and functions
from flask import Flask, jsonify, request, url_for
from flask_gzip import Gzip
from flask_htmlmin import HTMLMIN
from flask_caching import Cache
import os
import requests
import json
from datetime import datetime
import requests
import youtube_dl
import random 
import re
from custom_youtube import CustomYouTube
from requests.auth import HTTPProxyAuth

# creating a Flask app
application= Flask(__name__)
gzip = Gzip(application)

application.config['MINIFY_HTML'] = True
htmlmin = HTMLMIN(application)

# Configure caching
application.config['CACHE_TYPE'] = 'simple'
cache = Cache(application)

@application.route("/", methods = ["GET", "POST"])
def home():
	if(request.method == "GET"):

		data = "hello world"
		return jsonify({"data": data})
@application.route("/home", methods = ["GET"])
# @cache.cached(timeout=1284300, key_prefix=lambda: request.full_path)
def scrap_reels():
    proxies = (  
    "http://ewyhwkqa:989msyg77vq2@185.199.229.156:7492",
    "http://ewyhwkqa:989msyg77vq2@185.199.228.220:7300",
    "http://ewyhwkqa:989msyg77vq2@185.199.231.45:8382",
    "http://ewyhwkqa:989msyg77vq2@188.74.210.207:6286",
    "http://ewyhwkqa:989msyg77vq2@188.74.183.10:8279",
    "http://ewyhwkqa:989msyg77vq2@188.74.210.21:6100",
    "http://ewyhwkqa:989msyg77vq2@45.155.68.129:8133",
    "http://ewyhwkqa:989msyg77vq2@154.95.36.199:6893",
    "http://ewyhwkqa:989msyg77vq2@45.94.47.66:8110"

    )
    pr_oxy = [0,1,2,3,4,5,6,7,8]
    index = random.choice(pr_oxy)
    proxyDict = {"http" : proxies[index], "https" : proxies[index]}
    a = {"csrftoken":"JIzYAn9hVRjoDdNIQnLsqFCoVouO1WMC","sessionid":"53168773914%3AD0YRVq8KvrDZCf%3A15%3AAYeyRlmOZf2XHeCEuLrRfccq-JNAPqUO9PMiBSRIsA"}#rocky__8081  Ashar123
    b =  {"csrftoken":"1jwyJ5QczmCIva5ROe2OOj8opDwazXL3","sessionid":"36744979802%3AmISFYgnEY22rzr%3A20%3AAYc4E5uksgDF77ikhfeHkkTbGplkf92-acsJYzzptQ"} #farzi_kalosxyz  246800
    d =  {"csrftoken":"dv7osDMXDhLX2lTOsbPPnQ4gBNDPsG3O","sessionid":"58499749216%3AnDhC7Z4zEP6AWi%3A17%3AAYeZCANvuq3KMl40YjQNMB_GLZS5VkIKpGmVO_BqtQ"} #amsterdam34158 Amaan@123
    e =  {"csrftoken":"A6ledrZ83DJGCvmDYfF3vTIHQG1LOaCJ","sessionid":"53168773914%3Aafljno0aL18bpZ%3A23%3AAYcQfhhvaU7HHcy3YwKtp0x5bUbznwbsyqeKNMtYvw"}   #farzi_kalosxyz 246800
    f =  {"csrftoken":"yG0qeT6AdwIO2gUFLGSjvtYFYxhwA8eO","sessionid":"53168773914%3AiTndpEqqT0utPz%3A26%3AAYfZvE4oVH6l2zLFObt5svVqXXKFFJoAVk0uZ0pFjg"} #farzi_kalosxyz  246800   
    g =  {"csrftoken":"0KDtcmLuS6S5piO0dJkTLZd5J8SAb8o3","sessionid":"53168773914%3Ag8rfaOhrydC3XF%3A3%3AAYc2B6nN_8PwOUgla2ZxAwGyYhnLXypui8fyQtXpbQ"} #farzi_kalosxyz  246800   
    c= [a,e,f,g]
    cookie_jar = random.choice(c)
    headers = {
            "user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; motorola one Build/OPKS28.63-18-3; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.80 Mobile Safari/537.36 Instagram 72.0.0.21.98 Android (27/8.1.0; 320dpi; 720x1362; motorola; motorola one; deen_sprout; qcom; pt_BR; 132081645)",

         }
    csrf_token = cookie_jar["csrftoken"]
    session_id = cookie_jar["sessionid"]
    source = request.args["source"] 
    target = format(source)
    if target[:31] == "https://www.instagram.com/reel/" :
     cut_s = target[31:]
     separator = "/"
     cut_reel = cut_s.split(separator, 1)[0] 

     user_id_req = requests.get(f"https://www.instagram.com/p/{cut_reel}/?__a=1&__d=dis",headers=headers, cookies=cookie_jar, ).json()
     meta = {
              "posts": user_id_req,
              "cookie_jar":cookie_jar,
              "ip": proxyDict
           }      
    elif target[:32] == "https://www.instagram.com/reels/" :
     cut_s = target[32:]
     separator = "/"
     cut_reel = cut_s.split(separator, 1)[0] 

     user_id_req = requests.get(f"https://www.instagram.com/p/{cut_reel}/?__a=1&__d=dis",headers=headers, cookies=cookie_jar, ).json()
     meta = {
              "posts": user_id_req,
              "cookie_jar":cookie_jar,
              "ip": proxyDict
           }        
    elif target[:28] == "https://www.instagram.com/p/":
     cut_s = target[28:]
     separator = "/"
     cut_post = cut_s.split(separator, 1)[0] 
     user_id_req = requests.get(f"https://www.instagram.com/p/{cut_post}/?__a=1&__d=dis",headers=headers, cookies=cookie_jar, ).json()
     meta = {
        "posts": user_id_req,
        }
    elif target[:34] == "https://www.instagram.com/stories/" :
      cut_s = target[34:]
      separator = "/"
      cut_story = cut_s.split(separator, 1)[0] 
      user_id = requests.get(f"https://www.instagram.com/{cut_story}/?__a=1&__d=dis",headers=headers, cookies=cookie_jar, ).json()
      uniqid = user_id["graphql"]["user"]["id"] 
      user_id_req = requests.get(f"https://www.instagram.com/api/v1/feed/reels_media/?reel_ids={uniqid}",headers=headers, cookies=cookie_jar, ).json()
      is_priv = user_id_req["reels"][uniqid]['user']["is_private"]
    #   uniqid = user_id["graphql"]["user"]["id"] 
      if is_priv == True:
         meta = {
        "account": is_priv,
       }
      elif is_priv == False:   
    #    user_id_req = requests.get(f"https://www.instagram.com/api/v1/feed/reels_media/?reel_ids={uniqid}",headers=headers, cookies=cookie_jar, ).json()
       meta = {
        "story": user_id_req,
        "uniqid":uniqid,
        "account": is_priv,
       }   
    elif target[:30] == "https://instagram.com/stories/" :
      cut_s = target[30:]
      separator = "/"
      cut_story = cut_s.split(separator, 1)[0]  
      user_id = requests.get(f"https://www.instagram.com/{cut_story}/?__a=1&__d=dis",headers=headers, cookies=cookie_jar, ).json()
      uniqid = user_id["graphql"]["user"]["id"] 
      user_id_req = requests.get(f"https://www.instagram.com/api/v1/feed/reels_media/?reel_ids={uniqid}",headers=headers, cookies=cookie_jar, ).json()
      is_priv = user_id_req["reels"][uniqid]['user']["is_private"]
    #   uniqid = user_id["graphql"]["user"]["id"] 
      if is_priv == True:
         meta = {
        "account": is_priv,
       }
      elif is_priv == False:   
    #    user_id_req = requests.get(f"https://www.instagram.com/api/v1/feed/reels_media/?reel_ids={uniqid}",headers=headers, cookies=cookie_jar, ).json()
       meta = {
        "story": user_id_req,
        "uniqid":uniqid,
        "account": is_priv,
       }          
    elif target[:33] == "https://www.facebook.com/watch?v=" or target[:17] == "https://fb.watch/" or target[:24] == "https://www.facebook.com":
        ydl_opts = {}
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
          info = ydl.extract_info(target, download=False)
        meta = {
            "ytdll": info,
        }
    else:
         patterns =  [r'\?v=([A-Za-z0-9_-]+)', r'youtu\.be/([A-Za-z0-9_-]+)',  r'shorts/([A-Za-z0-9_-]+)', r'live/([A-Za-z0-9_-]+)',r'embed/([A-Za-z0-9_-]+)' ]
         for pattern in patterns:
            match = re.search(pattern, target)
            if match:
               cut = match.group(1)
         url = "https://www.youtube.com/youtubei/v1/player?key=AIzaSyAO_FJ2SlqU8Q4STEHLGCilw_Y9_11qcW8"
         payload = {
                  "videoId": cut,
                  "context": {
                     "client": {
                           "clientName": "ANDROID",
                           "clientVersion": "17.31.35",
                           "androidSdkVersion": 30} }}
         headers = {
                
                  "User-Agent" : "com.google.android.youtube/17.36.4 (Linux; U; Android 12; GB) gzip",
                              }

         response = requests.post(url, json=payload, headers=headers).json()
         duration = response['videoDetails']['lengthSeconds']
         duration = float(duration)
         if duration > 60  and duration <= 3600:
            minute = (duration/60)
            sec = round((minute%1)*60)
            sec = str(sec)
            if len(str(sec)) == 1:
               minute = str(int(minute))
               length = ":0".join([minute, sec])
            else:    
               minute = str(int(minute))
               length = ":".join([minute, sec])
         elif len(str(duration)) >= 4:
            hr = (duration/60)/60
            sec = round(((duration/60)%1)*60)
            nt = round((hr%1)*60)
            minute = str(nt)
            sec = str(sec)
            hr = str(int(hr))
            lengthh = ":".join([hr, minute])
            length =  ":".join([lengthh, sec])
         elif duration == 60:
            length = duration/60
            length = str(round(length))+":00"     
         else:
            length = "00:"+str(duration) 
         meta = {
            "response":response,
            "length":length,
         }
         return jsonify(meta)       
    if target[:32] == "https://www.youtube.com/watch?v=" or target[:31] == "https://www.youtube.com/shorts/" or target[:27] == "https://youtube.com/shorts/" or target[:17] == "https://youtu.be/" or target[:30] == "https://www.youtube.com/embed/" or  target[:29] == "https://www.youtube.com/live/" or target[:22] == "https://m.youtube.com/":
       return jsonify(meta)   
    else:

       return jsonify(meta)
#http://127.0.0.1:5000/home?source=https://www.facebook.com/watch?v=1245895546280667
@application.route("/story", methods = ["GET"])
@cache.cached(timeout=87000, key_prefix=lambda: request.full_path)
def reels():
    a = {"csrftoken":"0grbu9RmhEzqUZcdeSzhWNPIP6jonOcJ","sessionid":"53168773914%3ALoTkghbrxLAWd6%3A12%3AAYfKU1OLAcFKBv36pEhphkV-5RHVoU5NI6JeqV2m5A"}#rocky__8081  Ashar123
    b =  {"csrftoken":"1jwyJ5QczmCIva5ROe2OOj8opDwazXL3","sessionid":"36744979802%3AmISFYgnEY22rzr%3A20%3AAYc4E5uksgDF77ikhfeHkkTbGplkf92-acsJYzzptQ"} #farzi_kalosxyz  246800
    d =  {"csrftoken":"qwykHEl2NLWx7WMx0zvfl2SPMyeuyzt7","sessionid":"58499749216%3AkSPw4nLfRK4cbu%3A16%3AAYcLiiYD3HHBuBQcZ_jRNkeV5JmtBbJooIBBmNTT0w"} #amsterdam34158 Ammu123
    e =  {"csrftoken":"A6ledrZ83DJGCvmDYfF3vTIHQG1LOaCJ","sessionid":"53168773914%3Aafljno0aL18bpZ%3A23%3AAYcQfhhvaU7HHcy3YwKtp0x5bUbznwbsyqeKNMtYvw"}   #farzi_kalosxyz 246800
    f =  {"csrftoken":"yG0qeT6AdwIO2gUFLGSjvtYFYxhwA8eO","sessionid":"53168773914%3AiTndpEqqT0utPz%3A26%3AAYfZvE4oVH6l2zLFObt5svVqXXKFFJoAVk0uZ0pFjg"} #farzi_kalosxyz  246800   
    g =  {"csrftoken":"0KDtcmLuS6S5piO0dJkTLZd5J8SAb8o3","sessionid":"53168773914%3Ag8rfaOhrydC3XF%3A3%3AAYc2B6nN_8PwOUgla2ZxAwGyYhnLXypui8fyQtXpbQ"} #farzi_kalosxyz  246800   

   #  proxy_host = 'us.premium-residential.geonode.com'
   #  c = [9000,9001,9002,9003,9004,9005,9006,9007,9008,9009,9010]
   #  proxy_port = random.choice(c)
   #  proxy_username = 'geonode_YN5Sdft28N'
   #  proxy_password = '89736ca0-bfba-4f12-85d8-91e2af351d74'
   #  proxy_auth = HTTPProxyAuth(proxy_username, proxy_password)
    proxy_host = 'p.webshare.io'
    proxy_port = '80'
    prefix = "xlqlutuh-us"
    random_number = random.randint(1, 50000)
    proxy_username = f"{prefix}-{random_number}"
   #  proxy_username = 'xlqlutuh-us-1'
    proxy_password = 'g64kgmh8afoh'
    proxy_auth = HTTPProxyAuth(proxy_username, proxy_password)
    proxy = {
    'http': f'http://{proxy_username}:{proxy_password}@{proxy_host}:{proxy_port}/',
    'https': f'http://{proxy_username}:{proxy_password}@{proxy_host}:{proxy_port}/',
     }

    proxies = (  
    "http://58.124.251.164/",
   #  "http://ewyhwkqa:989msyg77vq2@185.199.229.156:7492",
      #  "http://ewyhwkqa:989msyg77vq2@185.199.229.156:7492",
   #  "http://ewyhwkqa:989msyg77vq2@185.199.228.220:7300",
   #  "http://ewyhwkqa:989msyg77vq2@185.199.231.45:8382",
   #  "http://ewyhwkqa:989msyg77vq2@188.74.210.207:6286",
   #  "http://ewyhwkqa:989msyg77vq2@188.74.183.10:8279",
   #  "http://ewyhwkqa:989msyg77vq2@188.74.210.21:6100",
   #  "http://ewyhwkqa:989msyg77vq2@45.155.68.129:8133",
   #  "http://ewyhwkqa:989msyg77vq2@154.95.36.199:6893",
   #  "http://ewyhwkqa:989msyg77vq2@45.94.47.66:8110"
    )
    pr_oxy = [0]
    index = random.choice(pr_oxy)
    proxyDict = {"http" : proxies[index], "https" : proxies[index]}
    c= [a]
    cookie_jar = random.choice(c)
    source = request.args["source"] 
    target = format(source)
    headers = {
            "Host": "www.instagram.com",
            "Origin": "https://www.instagram.com",
            "Referer": target,
            "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_6 like Mac OS X) AppleWebKit/604.5.6 (KHTML, like Gecko) Mobile/15D100 Instagram 37.0.0.9.96 (iPhone7,2; iOS 11_2_6; pt_PT; pt-PT; scale=2.34; gamut=normal; 750x1331) 12",

         }
    csrf_token = cookie_jar["csrftoken"]
    session_id = cookie_jar["sessionid"]

    if target[:34] == "https://www.instagram.com/stories/" : 
      while True:
         cut_s = target[34:]
         separator = "/"

         cut_story = cut_s.split(separator, 1)[0]  
         user_id_response = requests.get(f"https://i.instagram.com/api/v1/users/web_profile_info/?username={cut_story}",headers=headers, cookies=cookie_jar).json()
         uniqid = user_id_response["data"]["user"]["id"]
         user_id_req_response = requests.get(f"https://www.instagram.com/api/v1/feed/reels_media/?reel_ids={uniqid}",headers=headers, cookies=cookie_jar).json()

         is_priv = user_id_req_response["reels"][uniqid]['user']["is_private"]
         if user_id_req_response["reels"] != "":
           break  # Break the loop if status code is 200
         elif user_id_req_response["reels"] == "":
           continue  # Retry the request if status code is 304

      if is_priv == True:
         meta = {
        "account": is_priv,
       }
      elif is_priv == False:   
    #    user_id_req = requests.get(f"https://www.instagram.com/api/v1/feed/reels_media/?reel_ids={uniqid}",headers=headers, cookies=cookie_jar ).json()
       meta = {
        "story": user_id_req_response,
        "uniqid":uniqid,
        "account": is_priv,
        "username": proxy_username,
       }   
    elif target[:30] == "https://instagram.com/stories/" :
      while True:
         cut_s = target[30:]
         separator = "/"

         cut_story = cut_s.split(separator, 1)[0]  
         user_id_response = requests.get(f"https://i.instagram.com/api/v1/users/web_profile_info/?username={cut_story}",headers=headers, cookies=cookie_jar).json()
         uniqid = user_id_response["data"]["user"]["id"]
         user_id_req_response = requests.get(f"https://www.instagram.com/api/v1/feed/reels_media/?reel_ids={uniqid}",headers=headers, cookies=cookie_jar).json()

         is_priv = user_id_req_response["reels"][uniqid]['user']["is_private"]
         if user_id_req_response["reels"] != "":
           break  # Break the loop if status code is 200
         elif user_id_req_response["reels"] == "":
           continue  # Retry the request if status code is 304

      if is_priv == True:
         meta = {
        "account": is_priv,
       }
      elif is_priv == False:   
    #    user_id_req = requests.get(f"https://www.instagram.com/api/v1/feed/reels_media/?reel_ids={uniqid}",headers=headers, cookies=cookie_jar ).json()
       meta = {
        "story": user_id_req_response,
        "uniqid":uniqid,
        "account": is_priv,
        "username": proxy_username,
       }   
    elif target[:31] == "https://www.instagram.com/reel/" :
         cut_s = target[31:]
         separator = "/"
         cut_reel = cut_s.split(separator, 1)[0] 
         user_id_req = requests.get(f"https://www.instagram.com/graphql/query?query_hash=2b0673e0dc4580674a88d426fe00ea90&variables=%7B%22shortcode%22%3A%22{cut_reel}%22%7D",headers=headers, cookies=cookie_jar).json()
         meta = {
                  "posts": user_id_req,
                  "cookie_jar":cookie_jar,
                  "ip": proxyDict,
               }   
    elif target[:32] == "https://www.instagram.com/reels/" :
         cut_s = target[32:]
         separator = "/"
         cut_reel = cut_s.split(separator, 1)[0] 
         user_id_req = requests.get(f"https://www.instagram.com/graphql/query?query_hash=2b0673e0dc4580674a88d426fe00ea90&variables=%7B%22shortcode%22%3A%22{cut_reel}%22%7D",headers=headers , cookies=cookie_jar).json()
         meta = {
                  "posts": user_id_req,
                  "cookie_jar":cookie_jar,
                  "ip": proxyDict,
               }       
    elif target[:28] == "https://www.instagram.com/p/":
         cut_s = target[28:]
         separator = "/"
         cut_reel = cut_s.split(separator, 1)[0] 
         user_id_req = requests.get(f"https://www.instagram.com/graphql/query?query_hash=2b0673e0dc4580674a88d426fe00ea90&variables=%7B%22shortcode%22%3A%22{cut_reel}%22%7D",headers=headers ,cookies=cookie_jar).json()
         meta = {
            "posts": user_id_req,
            }         
    elif target[:32] == "https://www.youtube.com/watch?v=" or target[:31] == "https://www.youtube.com/shorts/" or target[:27] == "https://youtube.com/shorts/" or target[:17] == "https://youtu.be/":
         # url = "https://www.youtube.com/watch?v=11OWuPcElJw"   
         # age restricted
         # url = "https://www.youtube.com/watch?v=OQPYLFUKnVc"
         # video = YouTube(url,use_oauth=True, allow_oauth_cache=False)
      # cut = target[-11:]
      url = target
      video = CustomYouTube(url,use_oauth=False,allow_oauth_cache=True)
      video.bypass_age_gate()
      duration = video.length
      title = video.title
      thumbnail = video.thumbnail_url
      separator = "/"
      thumbnail = thumbnail.split(separator, 5)[4]
      if duration > 60  and duration <= 3600:
         minute = (duration/60)
         sec = round((minute%1)*60)
         sec = str(sec)
         if len(str(sec)) == 1:
            minute = str(int(minute))
            length = ":0".join([minute, sec])
         else:    
            minute = str(int(minute))
            length = ":".join([minute, sec])
      elif len(str(duration)) >= 4:
         hr = (duration/60)/60
         sec = round(((duration/60)%1)*60)
         nt = round((hr%1)*60)
         minute = str(nt)
         sec = str(sec)
         hr = str(int(hr))
         lengthh = ":".join([hr, minute])
         length =  ":".join([lengthh, sec])
      elif duration == 60:
         length = duration/60
         length = str(round(length))+":00"     
      else:
         length = "00:"+str(duration) 
      streams_720p = video.streams.filter(progressive=True,res='720p',audio_codec="mp4a.40.2")
      streams_720p_download = video.streams.filter(progressive=True,res='720p',audio_codec="mp4a.40.2")
      streams_360p = video.streams.filter(progressive=True,res='360p',audio_codec="mp4a.40.2")
      streams_144p = video.streams.filter(progressive=True,res='144p',audio_codec="mp4a.40.2")
      streams_2160p_mp4 = video.streams.filter(progressive=False,res='2160p')
      streams_1440p_mp4 = video.streams.filter(progressive=False,res='1440p')
      streams_1080p_mp4 = video.streams.filter(progressive=False,res='1080p',mime_type='video/mp4')
      streams_audio_mp4 = video.streams.filter(progressive=False,mime_type='audio/mp4')
      streams_720p_mp4 = video.streams.filter(adaptive=True,res='720p',mime_type='video/mp4')
      streams_480p_mp4 = video.streams.filter(progressive=False,res='480p',mime_type='video/mp4')
      streams_360p_mp4 = video.streams.filter(adaptive=True,res='360p',mime_type='video/mp4')
      streams_240p_mp4 = video.streams.filter(progressive=False,res='240p',mime_type='video/mp4')
      streams_144p_mp4 = video.streams.filter(progressive=False,res='144p',mime_type='video/mp4')
      streams_audio_128 = video.streams.filter(progressive=False,mime_type='audio/mp4', abr='128kbps')
      # streams_audio_48 = video.streams.filter(progressive=False,mime_type='audio/mp4', abr='48kbps')
      if len(streams_2160p_mp4) > 0 :
         meta = {'adaptive_formats_mp4':{ 
                        '0':{
                            'quality': '2160p',
                            'mime_type': 'video/mp4',
                            'url': streams_2160p_mp4.first().url,},'1':{
                            'quality': '1440p',
                            'mime_type': 'video/mp4',
                            'url': streams_1440p_mp4.first().url,},'2':{
                            'quality': '1080p',
                            'mime_type': 'video/mp4',
                            'url': streams_1080p_mp4.first().url,},'3':{
                            'quality': '720p',
                            'mime_type': 'video/mp4',
                            'url': streams_720p_mp4.first().url,},'4':{
                            'quality': '480p',
                            'mime_type': 'video/mp4',
                            'url': streams_480p_mp4.first().url,},'5':{
                            'quality': '360p',
                            'mime_type': 'video/mp4',
                            'url': streams_360p_mp4.first().url,},'6':{
                            'quality': '240p',
                            'mime_type': 'video/mp4',
                            'url': streams_240p_mp4.first().url,},'7':{
                            'quality': '144p',
                            'mime_type': 'video/mp4',
                            'url': streams_144p_mp4.first().url,},},
                    'formats':{'22':{
                        'quality': '720p',
                        'mime_type': 'video/mp4',
                        'url': streams_720p.first().url,},'18':{
                        'quality': '360p',
                        'mime_type': 'video/mp4',
                        'url': streams_360p.first().url,},'17':{
                        'quality': '144p',
                        'mime_type': 'video/mp4',
                        'url': streams_144p.first().url,},'audio_128':{
                        'quality': '128kbps',
                        'mime_type': 'audio/mp4',
                        'url': streams_audio_128.first().url, },
                        # 'audio_48':{
                        # 'quality': '48kbps',
                        # 'mime_type': 'audio/mp4',
                        # 'url': streams_audio_48.first().url,
                        #  },
                        },
                    'title': title,
                    'duration': length,
                     'id':thumbnail ,}
         return jsonify(meta)   
      elif len(streams_1080p_mp4) > 0 :
         meta = {'adaptive_formats_mp4':{  '0':{
                            'quality': '1080p',
                            'mime_type': 'video/mp4',
                            'url': streams_1080p_mp4.first().url,},'1':{
                            'quality': '720p',
                            'mime_type': 'video/mp4',
                            'url': streams_720p_mp4.first().url,},'2':{
                            'quality': '480p',
                            'mime_type': 'video/mp4',
                            'url': streams_480p_mp4.first().url,},'3':{
                            'quality': '360p',
                            'mime_type': 'video/mp4',
                            'url': streams_360p_mp4.first().url,},'4':{
                            'quality': '240p',
                            'mime_type': 'video/mp4',
                            'url': streams_240p_mp4.first().url,},'5':{
                            'quality': '144p',
                            'mime_type': 'video/mp4',
                            'url': streams_144p_mp4.first().url,},},
                    'formats':{'22':{
                        'quality': '720p',
                        'mime_type': 'video/mp4',
                        'url': streams_720p.first().url,},'18':{
                        'quality': '360p',
                        'mime_type': 'video/mp4',
                        'url': streams_360p.first().url,},'17':{
                        'quality': '144p',
                        'mime_type': 'video/mp4',
                        'url': streams_144p.first().url,},'audio_128':{
                        'quality': '128kbps',
                        'mime_type': 'audio/mp4',
                        'url': streams_audio_128.first().url,},
                        # 'audio_48':{
                        # 'quality': '48kbps',
                        # 'mime_type': 'audio/mp4',
                        # 'url': streams_audio_48.first().url,},
                        },
                    'title': title,
                    'duration': length,
                     'id':thumbnail ,}
         return jsonify(meta)    
      elif  len(streams_720p_mp4) > 0:
         meta = {'adaptive_formats_mp4':{'0':{
                            'quality': '720p',
                            'mime_type': 'video/mp4',
                            'url': streams_720p_mp4.first().url,},'1':{
                            'quality': '480p',
                            'mime_type': 'video/mp4',
                            'url': streams_480p_mp4.first().url,},'2':{
                            'quality': '360p',
                            'mime_type': 'video/mp4',
                            'url': streams_360p_mp4.first().url,},'3':{
                            'quality': '240p',
                            'mime_type': 'video/mp4',
                            'url': streams_240p_mp4.first().url,},'4':{
                            'quality': '144p',
                            'mime_type': 'video/mp4',
                            'url': streams_144p_mp4.first().url,},},
                    'formats':{'22':{
                        'quality': '720p',
                        'mime_type': 'video/mp4',
                        'url': streams_720p.first().url,},'18':{
                        'quality': '360p',
                        'mime_type': 'video/mp4',
                        'url': streams_360p.first().url,},'17':{
                        'quality': '144p',
                        'mime_type': 'video/mp4',
                        'url': streams_144p.first().url,},'audio_128':{
                        'quality': '128kbps',
                        'mime_type': 'audio/mp4',
                        'url': streams_audio_128.first().url,},
                        # 'audio_48':{
                        # 'quality': '48kbps',
                        # 'mime_type': 'audio/mp4',
                        # 'url': streams_audio_48.first().url,},
                        },
                    'title': title,
                    'duration': length,
                     'id':thumbnail ,}
         return jsonify(meta)       

      elif len(streams_360p_mp4) > 0:
         meta = {'adaptive_formats_mp4':{'0':{
                            'quality': '360p',
                            'mime_type': 'video/mp4',
                            'url': streams_360p_mp4.first().url,},'1':{
                            'quality': '240p',
                            'mime_type': 'video/mp4',
                            'url': streams_240p_mp4.first().url,},'2':{
                            'quality': '144p',
                            'mime_type': 'video/mp4',
                            'url': streams_144p_mp4.first().url, },},
                    'formats':{'22':{
                        'quality': '720p',
                        'mime_type': 'video/mp4',
                        'url': streams_360p.first().url,},'18':{
                        'quality': '360p',
                        'mime_type': 'video/mp4',
                        'url': streams_360p.first().url,},'17':{
                        'quality': '144p',
                        'mime_type': 'video/mp4',
                        'url': streams_144p.first().url,},'audio_128':{
                        'quality': '128kbps',
                        'mime_type': 'audio/mp4',
                        'url': streams_audio_128.first().url,},
                        # 'audio_48':{
                        # 'quality': '48kbps',
                        # 'mime_type': 'audio/mp4',
                        # 'url': streams_audio_48.first().url,},
                         },
                    'title': title,
                    'duration': length,
                     'id':thumbnail ,
                    }    
         return jsonify(meta)

      # return jsonify(meta)
    else:   
      while True:
         cut_story= target

         user_id_response = requests.get(f"https://i.instagram.com/api/v1/users/web_profile_info/?username={cut_story}",headers=headers, cookies=cookie_jar).json()
         uniqid = user_id_response["data"]["user"]["id"]
         user_id_req_response = requests.get(f"https://www.instagram.com/api/v1/feed/reels_media/?reel_ids={uniqid}",headers=headers, cookies=cookie_jar).json()

         is_priv = user_id_req_response["reels"][uniqid]['user']["is_private"]
         if user_id_req_response["reels"] != "":
           break  # Break the loop if status code is 200
         elif user_id_req_response["reels"] == "":
           continue  # Retry the request if status code is 304

      if is_priv == True:
         meta = {
        "account": is_priv,
       }
      elif is_priv == False:   
    #    user_id_req = requests.get(f"https://www.instagram.com/api/v1/feed/reels_media/?reel_ids={uniqid}",headers=headers, cookies=cookie_jar ).json()
       meta = {
        "story": user_id_req_response,
        "uniqid":uniqid,
        "account": is_priv,
        "username": proxy_username,
       }   
    if target[:32] == "https://www.youtube.com/watch?v=" or target[:31] == "https://www.youtube.com/shorts/" or target[:27] == "https://youtube.com/shorts/" or target[:17] == "https://youtu.be/" or target[:29] == "https://www.youtube.com/live/": 
    
       return (meta)
        
    else:

      return jsonify(meta)
# driver function

@application.route("/audio", methods = ["GET"])
@cache.cached(timeout=87000, key_prefix=lambda: request.full_path)
def audio():
    a = {"csrftoken":"0grbu9RmhEzqUZcdeSzhWNPIP6jonOcJ","sessionid":"53168773914%3ALoTkghbrxLAWd6%3A12%3AAYfKU1OLAcFKBv36pEhphkV-5RHVoU5NI6JeqV2m5A"}#rocky__8081  Ashar123
    b =  {"csrftoken":"1jwyJ5QczmCIva5ROe2OOj8opDwazXL3","sessionid":"36744979802%3AmISFYgnEY22rzr%3A20%3AAYc4E5uksgDF77ikhfeHkkTbGplkf92-acsJYzzptQ"} #farzi_kalosxyz  246800
    d =  {"csrftoken":"qwykHEl2NLWx7WMx0zvfl2SPMyeuyzt7","sessionid":"58499749216%3AkSPw4nLfRK4cbu%3A16%3AAYcLiiYD3HHBuBQcZ_jRNkeV5JmtBbJooIBBmNTT0w"} #amsterdam34158 Ammu123
    e =  {"csrftoken":"A6ledrZ83DJGCvmDYfF3vTIHQG1LOaCJ","sessionid":"53168773914%3Aafljno0aL18bpZ%3A23%3AAYcQfhhvaU7HHcy3YwKtp0x5bUbznwbsyqeKNMtYvw"}   #farzi_kalosxyz 246800
    f =  {"csrftoken":"yG0qeT6AdwIO2gUFLGSjvtYFYxhwA8eO","sessionid":"53168773914%3AiTndpEqqT0utPz%3A26%3AAYfZvE4oVH6l2zLFObt5svVqXXKFFJoAVk0uZ0pFjg"} #farzi_kalosxyz  246800   
    g =  {"csrftoken":"0KDtcmLuS6S5piO0dJkTLZd5J8SAb8o3","sessionid":"53168773914%3Ag8rfaOhrydC3XF%3A3%3AAYc2B6nN_8PwOUgla2ZxAwGyYhnLXypui8fyQtXpbQ"} #farzi_kalosxyz  246800   
   
   #  proxy_host = 'us.premium-residential.geonode.com'
   #  c = [9000,9001,9002,9003,9004,9005,9006,9007,9008,9009,9010]
   #  proxy_port = random.choice(c)
   #  proxy_username = 'geonode_YN5Sdft28N'
   #  proxy_password = '89736ca0-bfba-4f12-85d8-91e2af351d74'
   #  proxy_auth = HTTPProxyAuth(proxy_username, proxy_password)
    proxy_host = 'p.webshare.io'
    proxy_port = '80'
    prefix = "xlqlutuh-us"
    random_number = random.randint(1, 5000)
    proxy_username = f"{prefix}-{random_number}"
   #  proxy_username = 'xlqlutuh-us-1'
    proxy_password = 'g64kgmh8afoh'
    proxy_auth = HTTPProxyAuth(proxy_username, proxy_password)
    proxy = {
    'http': f'http://{proxy_username}:{proxy_password}@{proxy_host}:{proxy_port}/',
    'https': f'http://{proxy_username}:{proxy_password}@{proxy_host}:{proxy_port}/',
     }

    proxies = (  
    "http://58.124.251.164/",
   #  "http://ewyhwkqa:989msyg77vq2@185.199.229.156:7492",
   #  "http://ewyhwkqa:989msyg77vq2@185.199.228.220:7300",
   #  "http://ewyhwkqa:989msyg77vq2@185.199.231.45:8382",
   #  "http://ewyhwkqa:989msyg77vq2@188.74.210.207:6286",
   #  "http://ewyhwkqa:989msyg77vq2@188.74.183.10:8279",
   #  "http://ewyhwkqa:989msyg77vq2@188.74.210.21:6100",
   #  "http://ewyhwkqa:989msyg77vq2@45.155.68.129:8133",
   #  "http://ewyhwkqa:989msyg77vq2@154.95.36.199:6893",
   #  "http://ewyhwkqa:989msyg77vq2@45.94.47.66:8110"

    )
    pr_oxy = [0]
    index = random.choice(pr_oxy)
    proxyDict = {"http" : proxies[index], "https" : proxies[index]}
    c= [a]
    cookie_jar = random.choice(c)
    source = request.args["source"] 
    target = format(source)
    headers = {
            "Host": "www.instagram.com",
            "Origin": "https://www.instagram.com",
            "Referer": target,
            "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_6 like Mac OS X) AppleWebKit/604.5.6 (KHTML, like Gecko) Mobile/15D100 Instagram 37.0.0.9.96 (iPhone7,2; iOS 11_2_6; pt_PT; pt-PT; scale=2.34; gamut=normal; 750x1331) 12"
         }
    csrf_token = cookie_jar["csrftoken"]
    session_id = cookie_jar["sessionid"]
     
    if target[:34] == "https://www.instagram.com/stories/" :
      cut_s = target[34:]
      separator = "/"

      cut_story = cut_s.split(separator, 1)[0]  
      user_id = requests.get(f"https://i.instagram.com/api/v1/users/web_profile_info/?username={cut_story}",headers=headers, cookies=cookie_jar).json()
      uniqid = user_id["data"]["user"]["id"]  
      user_id_req = requests.get(f"https://www.instagram.com/api/v1/feed/reels_media/?reel_ids={uniqid}",headers=headers, cookies=cookie_jar).json()
 
      is_priv = user_id_req["reels"][uniqid]['user']["is_private"]
      pattern = r'\d+'
      match = re.search(pattern, target)
      if match:
         numbers = match.group()
         print(numbers)
      else:
         print("No numbers found in the URL.")
      items = user_id_req["reels"][uniqid]["items"]
      for item in items:
        if item["id"][:19] == numbers:
         audio = item["video_dash_manifest"]
         thumbnail = item["image_versions2"]["candidates"][0]["url"]
         pattern = r'<AudioChannelConfiguration schemeIdUri="urn:mpeg:dash:23003:3:audio_channel_configuration:2011" value="2"/><BaseURL>(.*?)<\/BaseURL>'
         match = re.search(pattern, audio)
         audio_url = match.group(1)
         url = re.sub(r'&amp;', '&', audio_url)
    #   uniqid = user_id["graphql"]["user"]["id"] 
      if is_priv == True:
         meta = {
        "account": is_priv,
       }
      elif is_priv == False:   
    #    user_id_req = requests.get(f"https://www.instagram.com/api/v1/feed/reels_media/?reel_ids={uniqid}",headers=headers, cookies=cookie_jar ).json()
       meta = {
        "story": user_id_req,
        "uniqid":uniqid,
        "account": is_priv,
        "audio_url": url,
        "thumbnail": thumbnail,
       }  
       return jsonify(meta)    
    elif target[:30] == "https://instagram.com/stories/" :
      cut_s = target[30:]
      separator = "/"

      cut_story = cut_s.split(separator, 1)[0]  
      user_id = requests.get(f"https://i.instagram.com/api/v1/users/web_profile_info/?username={cut_story}",headers=headers, cookies=cookie_jar).json()
      uniqid = user_id["data"]["user"]["id"] 
      user_id_req = requests.get(f"https://www.instagram.com/api/v1/feed/reels_media/?reel_ids={uniqid}",headers=headers, cookies=cookie_jar).json()
 
      is_priv = user_id_req["reels"][uniqid]['user']["is_private"]
      pattern = r'\d+'
      match = re.search(pattern, target)
      if match:
         numbers = match.group()
         print(numbers)
      else:
         print("No numbers found in the URL.")
      items = user_id_req["reels"][uniqid]["items"]
      for item in items:
        if item["id"][:19] == numbers:
         audio = item["video_dash_manifest"]
         thumbnail = item["image_versions2"]["candidates"][0]["url"]
         pattern = r'<AudioChannelConfiguration schemeIdUri="urn:mpeg:dash:23003:3:audio_channel_configuration:2011" value="2"/><BaseURL>(.*?)<\/BaseURL>'
         match = re.search(pattern, audio)
         audio_url = match.group(1)
         url = re.sub(r'&amp;', '&', audio_url)
    #   uniqid = user_id["graphql"]["user"]["id"] 
      if is_priv == True:
         meta = {
        "account": is_priv,
       }
      elif is_priv == False:   
    #    user_id_req = requests.get(f"https://www.instagram.com/api/v1/feed/reels_media/?reel_ids={uniqid}",headers=headers, cookies=cookie_jar ).json()
       meta = {
        "story": user_id_req,
        "uniqid":uniqid,
        "account": is_priv,
        "audio_url": url,
       "thumbnail":thumbnail,
       }
       return jsonify(meta) 
    elif target[:31] == "https://www.instagram.com/reel/" :
         cut_s = target[31:]
         separator = "/"
         cut_reel = cut_s.split(separator, 1)[0] 
         user_id_req = requests.get(f"https://www.instagram.com/graphql/query?query_hash=2b0673e0dc4580674a88d426fe00ea90&variables=%7B%22shortcode%22%3A%22{cut_reel}%22%7D",headers=headers,cookies=cookie_jar).json()
         audio = user_id_req["data"]["shortcode_media"]["dash_info"]["video_dash_manifest"]
         pattern = r'<AudioChannelConfiguration schemeIdUri="urn:mpeg:dash:23003:3:audio_channel_configuration:2011" value="2"/><BaseURL>(.*?)<\/BaseURL>'
         match = re.search(pattern, audio)
         audio_url = match.group(1)
         url = re.sub(r'&amp;', '&', audio_url)
         meta = {
                  "posts": user_id_req,
                  "cookie_jar":cookie_jar,
                  "ip": proxyDict,
                  "audio_url": url,
               }  
         return jsonify(meta)          
    elif target[:32] == "https://www.instagram.com/reels/" :
         cut_s = target[32:]
         separator = "/"
         cut_reel = cut_s.split(separator, 1)[0] 
         user_id_req = requests.get(f"https://www.instagram.com/graphql/query?query_hash=2b0673e0dc4580674a88d426fe00ea90&variables=%7B%22shortcode%22%3A%22{cut_reel}%22%7D",headers=headers ,cookies=cookie_jar).json()
         audio = user_id_req["data"]["shortcode_media"]["dash_info"]["video_dash_manifest"]
         pattern = r'<AudioChannelConfiguration schemeIdUri="urn:mpeg:dash:23003:3:audio_channel_configuration:2011" value="2"/><BaseURL>(.*?)<\/BaseURL>'
         match = re.search(pattern, audio)
         audio_url = match.group(1)
         url = re.sub(r'&amp;', '&', audio_url)
         meta = {
                  "posts": user_id_req,
                  "cookie_jar":cookie_jar,
                  "ip": proxyDict,
                  "audio_url": url,
               }  
         return jsonify(meta)    
@application.route("/yt", methods = ["GET"])
# @cache.cached(timeout=87000, key_prefix=lambda: request.full_path)
def youtube():
   source = request.args["source"] 
   target = format(source)
   patterns =  [r'\?v=([A-Za-z0-9_-]+)', r'youtu\.be/([A-Za-z0-9_-]+)',  r'shorts/([A-Za-z0-9_-]+)', r'live/([A-Za-z0-9_-]+)',r'embed/([A-Za-z0-9_-]+)' ]
   for pattern in patterns:
            match = re.search(pattern, target)
            if match:
               cut = match.group(1)
   url = "https://www.youtube.com/youtubei/v1/player?key=AIzaSyAO_FJ2SlqU8Q4STEHLGCilw_Y9_11qcW8"
   payload = {
                  "videoId": cut,
                  "context": {
                     "client": {
                           "clientName": "ANDROID_CREATOR",
                           "clientVersion": "22.30.100",
                           "androidSdkVersion": 30,
                           "hl": "en-US",
                           "gl":"US",
                           } }}
   headers = {
                "User-Agent" : "com.google.android.apps.youtube.creator/ gzip",
                "Content-Type": "application/json",
                              }

   response = requests.post(url, json=payload, headers=headers).json()
   duration = response['videoDetails']['lengthSeconds']
   duration = float(duration)
   if duration > 60  and duration <= 3600:
      minute = (duration/60)
      sec = round((minute%1)*60)
      sec = str(sec)
      if len(str(sec)) == 1:
         minute = str(int(minute))
         length = ":0".join([minute, sec])
      else:    
         minute = str(int(minute))
         length = ":".join([minute, sec])
   elif len(str(duration)) >= 4:
      hr = (duration/60)/60
      sec = round(((duration/60)%1)*60)
      nt = round((hr%1)*60)
      minute = str(nt)
      sec = str(sec)
      hr = str(int(hr))
      lengthh = ":".join([hr, minute])
      length =  ":".join([lengthh, sec])
   elif duration == 60:
      length = duration/60
      length = str(round(length))+":00"     
   else:
      length = "00:"+str(duration) 
   meta = {
      "response":response,
      "length":length,
   }
   return jsonify(meta)   
if __name__ == "__main__":

	application.run(debug = True)
