import disnake
from disnake.ext import commands


class User(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name='user',description='Получите информацию о себе либо об участнике')
    async def user(self,inter, user: disnake.User = None):
        if user is None: user = inter.author
        embed = disnake.Embed(
            title='Информация об {}'.format(user.display_name),
            description='Основное: \n Имя: `{}` | {}  \n Айди: `{}` \n Роли: {}'.format(user.name,user.mention,user.id,user)
        )
        embed.set_image(url=user.banner)
        await inter.send(embed=embed)

    @commands.slash_command(name='ping',description='Пинг бота до серверов дискорда')
    async def ping(self,inter):
        await inter.send('`🎾` Задержка бота до серверов дискорда составляет **{} мс.**'.format(round(self.bot.latency * 1000)))

def setup(bot):
    bot.add_cog(User(bot))
    print('[!] Команды подгружены в память бота')
