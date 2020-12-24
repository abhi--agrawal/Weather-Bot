from replit import db
import random

def update_message(weather, message):
  db[weather].append(message)

def delete_message(weather, index):
  messages = db[weather]
  if len(messages) > index:
    del messages[index]
    db[weather] = messages

def get_random_message(weather):
  return random.choice(db[weather])

def get_all_messages(weather):
  return db[weather]

default = "Thats all you're going to get. Now go away let me rest."
#Cloudy
cloudy = [
"Just like your future.",
"A simp just like you.",
"It also cannot decide what it wanted to be, you dont have to feel left out",
"In all honesty the clouds do not want you to look at the stars",
default
]

#snow
snowy = [
"Elsa is throwing some tantrums, Disney will get is sorted soon, till then stay in.",
"Last time I checked you weren't a Polar Bear, so if you didn't somehow became an amimagus since then keep indoors",
default
]

#get_rain
rainy = [
"Get your umbrealla or rain coat or just fucking stay indoors, whatever.",
"great, now you can cancel all your plans without feeling guilty like you wanted to",
default
]

stormy = [default]

drizzle = [default]

misty = [default]

#temperature
"This temperature is proof that mother nature hates you."
"I hope you enjoy cold dark crap, if not too bad."

def init_db():
  db['cloudy'] = cloudy
  db['snowy'] = snowy
  db['rainy'] = rainy
  db['stormy'] = stormy
  db['drizzle'] = drizzle
  db['misty'] = misty
  