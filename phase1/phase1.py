#Variables, data types, operators, control structures
students={"Ahmed": 85,"Sara": 92, "Ali": 60,"Fatima": 78, "Umar": 45,}
fail_count=0;
for name, score in students.items():
    if score >= 90:
      print(f"{name}: A grade");
    elif score>= 80:
      print(f"{name}: B grade");
    elif score>= 70:
      print(f"{name}: C grade");
    elif score>= 60:
      print(f"{name}: D grade");
    else:
      print(f"{name}: Failing");
      fail_count+=1
      
      
print(f"Total failing: {fail_count}");

#Functions
def calculate_discount(price,discount_percent):
    return int(price-(price*discount_percent/100));

def print_receipt(name,final_price):
    print(f"{name} your final price is {final_price}")


print_receipt("Minahil",calculate_discount(1000,15))



#Classes and OOP
class BankAccount:
  def __init__(self,name,balance):
    self.name=name
    self.balance=balance
  def deposit(self,amount):
    self.balance+=amount
    print(f"{self.balance} new balance")
  def with_draw(self,amount):
    if (amount>self.balance):
      print("insufficient amount")
    else:
      self.balance-=amount
      print(f"{self.balance} new balance")
  def show_balance(self):
    print(f"{self.balance} current balance")
    
athar=BankAccount('Athar',300000)
print(athar.balance)
athar.deposit(100)
athar.with_draw(50)
athar.show_balance()

# second account
rahat = BankAccount("Rahat", 50000)
rahat.deposit(5000)
rahat.show_balance()



#Working with JSON data parsing, reading, writing
import json

# Python dictionary
person = {
    "name": "Minahil",
    "age": 22,
    "skills": ["Python", "LangChain"]
}

# Save to a JSON file
with open("data.json", "w") as f:
    json.dump(person, f, indent=4)
    
  # Read from a JSON file
with open("data.json", "r") as f:
    loaded = json.load(f)
    for skill in loaded["skills"]:
      print(skill)  
      

#HTTP requests using the requests library
import requests
url = "https://api.agify.io"

params={
  "name":"Minahil"
}

response = requests.get(url, params=params)
data=response.json()
print(data)
#-----------------------------------------------------------
url="https://official-joke-api.appspot.com/random_joke"
for i in range(3):
  response=requests.get(url)
  data=response.json()
  print(f"Type: {data['type']}")
  print(f"Setup: {data['setup']}")
  print(f"Punchline: {data['punchline']}")
  
  
#• Environment variables and .env files (python-dotenv)
from dotenv import load_dotenv
import os

# load the .env file
load_dotenv()

# read variables from it
name = os.getenv("YOUR_NAME")
city = os.getenv("CITY")
language= os.getenv("FAVOURITE_LANGUAGE")

print(f"My name is {name}, I am from {city} and my favourite language is {language} ")
  
#File handling read/write text, CSV, JSON files

  
    



















































