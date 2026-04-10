from dotenv import load_dotenv
import requests
import json
import os

class JokeFetcher:
  def __init__(self):
    load_dotenv()
    self.app_name = os.getenv("APP_NAME")
    with open('config.json', 'r') as file:
      config = json.load(file)
      self.joke_count = config["number"]
      self.joke_type = config["type"]
    
  
  def fetch_jokes(self):
      print(f"welcome to {self.app_name}")
      url="https://official-joke-api.appspot.com/random_joke"
      jokes=[]
      for i in range(self.joke_count):
          try:
              response = requests.get(url)
              response.raise_for_status()
              data = response.json()
              if data["type"] == self.joke_type:
                    jokes.append(data)
          except requests.exceptions.ConnectionError:
                print("No internet connection")
          except requests.exceptions.HTTPError as e:
                print(f"API error: {e}")
          except Exception as e:
                print(f"Something went wrong: {e}")
      return jokes
              
      
     
  def save_jokes(self,jokes):
      with open("jokes.txt", "w", newline="") as f:
             for joke in jokes:
                f.write(f"Type: {joke['type']}\n")
                f.write(f"Setup: {joke['setup']}\n")
                f.write(f"Punchline: {joke['punchline']}\n") 
             print(f"JokeFetcher fetched {self.joke_count} jokes and saved to jokes.txt")  
 

fetcher = JokeFetcher()
jokes = fetcher.fetch_jokes()
fetcher.save_jokes(jokes)

    
  
  
