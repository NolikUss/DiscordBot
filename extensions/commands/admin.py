import disnake
from disnake.ext import commands
from config import setting

class Admin(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name='bot-info',guild_ids=setting['testguild'],description='Получение основной информации о боте для разработчика.')
    async def info(self,inter: disnake.CommandInteraction):
        
        print('[!] Разработчик {} запросил информацию о боте, вывожу её в консоль'.format(inter.author.name))
        print('------ ПАНЕЛЬ ИНФОРМАЦИИ ------')
        print('Версия: {}'.format(setting['bot-version']))
        print('Айди бота: {}'.format(setting['botid']))
        print('Включено ли создание автоматических кастомных комнат: {}'.format(setting['disable-auto-rooms']))
        print('TOKEN: {}'.format(setting['token']))
        print('-------------------------------')
        await inter.send(content='{}, Информация была отправлена в консоль бота.'.format(inter.author.mention),ephemeral=True)

def setup(bot):
    bot.add_cog(Admin(bot))
