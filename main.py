import os
import disnake
from disnake.ext import commands
from config import setting


bot = commands.InteractionBot(owner_id=setting['ownerid'],)
    	
for cog in os.listdir('./extensions/cogs'):
    	if cog.endswith('.py'):
    		bot.load_extension(f'extensions.cogs.{cog[:-3]}')

for command in os.listdir('./extensions/commands'):
    	if command.endswith('.py'):
    			bot.load_extension(f'extensions.commands.{command[:-3]}')
    			
for event in os.listdir('./extensions/events'):
    	if event.endswith('.py'):
    			bot.load_extension(f'extensions.events.{event[:-3]}')

@bot.event
async def on_ready():
	print('[!] Бот запущен')
	

if __name__ == "__main__":
	bot.run(setting['token'])
