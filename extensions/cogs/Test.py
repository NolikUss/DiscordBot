import disnake
from disnake.ext import commands


class Test(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    @commands.slash_command(name='test',description='Проверка работы когов')
    async def test(self,inter):
        await inter.send('Всё работает!')




def setup(bot):
    bot.add_cog(Test(bot))
    print('[!] Коги загружены')