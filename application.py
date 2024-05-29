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
import random 
import re

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

@application.route("/story", methods = ["GET"])
@cache.cached(timeout=87000, key_prefix=lambda: request.full_path)
def reels():
    a = {"csrftoken":"0grbu9RmhEzqUZcdeSzhWNPIP6jonOcJ","sessionid":"53168773914%3ALoTkghbrxLAWd6%3A12%3AAYfKU1OLAcFKBv36pEhphkV-5RHVoU5NI6JeqV2m5A"}# Username= MKrocky__9964  Password= Vietnam3883
    b =  {"csrftoken":"1jwyJ5QczmCIva5ROe2OOj8opDwazXL3","sessionid":"36744979802%3AmISFYgnEY22rzr%3A20%3AAYc4E5uksgDF77ikhfeHkkTbGplkf92-acsJYzzptQ"} #farzi_kalosxyz  246800
    d =  {"csrftoken":"qwykHEl2NLWx7WMx0zvfl2SPMyeuyzt7","sessionid":"58499749216%3AkSPw4nLfRK4cbu%3A16%3AAYcLiiYD3HHBuBQcZ_jRNkeV5JmtBbJooIBBmNTT0w"} #amsterdam34158 amstew
    e =  {"csrftoken":"A6ledrZ83DJGCvmDYfF3vTIHQG1LOaCJ","sessionid":"53168773914%3Aafljno0aL18bpZ%3A23%3AAYcQfhhvaU7HHcy3YwKtp0x5bUbznwbsyqeKNMtYvw"}   #farzi_kalosxyz 246800
    f =  {"csrftoken":"yG0qeT6AdwIO2gUFLGSjvtYFYxhwA8eO","sessionid":"53168773914%3AiTndpEqqT0utPz%3A26%3AAYfZvE4oVH6l2zLFObt5svVqXXKFFJoAVk0uZ0pFjg"} #farzi_kalosxyz  246800   
    g =  {"csrftoken":"0KDtcmLuS6S5piO0dJkTLZd5J8SAb8o3","sessionid":"53168773914%3Ag8rfaOhrydC3XF%3A3%3AAYc2B6nN_8PwOUgla2ZxAwGyYhnLXypui8fyQtXpbQ"} #farzi_kalosxyz  246800   

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
      return jsonify(meta)

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
      return jsonify(meta)

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
         return jsonify(meta)
    
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
         return jsonify(meta)

    elif target[:28] == "https://www.instagram.com/p/":
         cut_s = target[28:]
         separator = "/"
         cut_reel = cut_s.split(separator, 1)[0] 
         user_id_req = requests.get(f"https://www.instagram.com/graphql/query?query_hash=2b0673e0dc4580674a88d426fe00ea90&variables=%7B%22shortcode%22%3A%22{cut_reel}%22%7D",headers=headers ,cookies=cookie_jar).json()
         meta = {
            "posts": user_id_req,
             }     
         return jsonify(meta)


  
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
      return jsonify(meta)

# driver function

@application.route("/audio", methods = ["GET"])
@cache.cached(timeout=87000, key_prefix=lambda: request.full_path)
def audio():
    a = {"csrftoken":"0grbu9RmhEzqUZcdeSzhWNPIP6jonOcJ","sessionid":"53168773914%3ALoTkghbrxLAWd6%3A12%3AAYfKU1OLAcFKBv36pEhphkV-5RHVoU5NI6JeqV2m5A"}# Username= MKrocky__9964  Password= Vietnam3883
    b =  {"csrftoken":"1jwyJ5QczmCIva5ROe2OOj8opDwazXL3","sessionid":"36744979802%3AmISFYgnEY22rzr%3A20%3AAYc4E5uksgDF77ikhfeHkkTbGplkf92-acsJYzzptQ"} #farzi_kalosxyz  246800
    d =  {"csrftoken":"qwykHEl2NLWx7WMx0zvfl2SPMyeuyzt7","sessionid":"58499749216%3AkSPw4nLfRK4cbu%3A16%3AAYcLiiYD3HHBuBQcZ_jRNkeV5JmtBbJooIBBmNTT0w"} #amsterdam34158 amstew
    e =  {"csrftoken":"A6ledrZ83DJGCvmDYfF3vTIHQG1LOaCJ","sessionid":"53168773914%3Aafljno0aL18bpZ%3A23%3AAYcQfhhvaU7HHcy3YwKtp0x5bUbznwbsyqeKNMtYvw"}   #farzi_kalosxyz 246800
    f =  {"csrftoken":"yG0qeT6AdwIO2gUFLGSjvtYFYxhwA8eO","sessionid":"53168773914%3AiTndpEqqT0utPz%3A26%3AAYfZvE4oVH6l2zLFObt5svVqXXKFFJoAVk0uZ0pFjg"} #farzi_kalosxyz  246800   
    g =  {"csrftoken":"0KDtcmLuS6S5piO0dJkTLZd5J8SAb8o3","sessionid":"53168773914%3Ag8rfaOhrydC3XF%3A3%3AAYc2B6nN_8PwOUgla2ZxAwGyYhnLXypui8fyQtXpbQ"} #farzi_kalosxyz  246800   
   

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

if __name__ == "__main__":

	application.run(debug = True)

