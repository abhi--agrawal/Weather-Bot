import discord as d
import os
import requests
import json
from keep_alive import keep_alive
from weather import get_cur_weather
from database import update_message

client = d.Client()

def get_quote():
  resp = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(resp.text)
  q = json_data[0]['q'] + ' - ' + json_data[0]['a']
  return q

@client.event
async def on_ready():
  print('We are logged in as {0.user}'.format(client))

@client.event
async def on_message(msg):
  if msg.author == client.user:
    return
  
  if msg.content.startswith('!Hello') or msg.content.startswith('!hello'):
    await msg.channel.send('Hello {0.author.name}. How you doing?'.format(msg))

  if msg.content.lower().startswith('!inspire'):
    await msg.channel.send(get_quote()) 

  if msg.content.lower().startswith('!weather'):
    loc = msg.content.lower().split(' ',1)
    await msg.channel.send(get_cur_weather(loc[1]))

  if msg.content.lower().startswith('!add-msg'):
    add_msg = msg.content.lower().split(' ',1)
    update_message('misty', add_msg)
    await msg.channel.send("Added")

keep_alive()
#init_db()
client.run(os.getenv('TOKEN'))