import disnake
from disnake.ext import commands
from captcha.image import ImageCaptcha
import os
import random
 
 
class Verif(disnake.ui.Select):
    def __init__(self,code) -> None:
        self.codes = list(code,random.randint(a=100000,b=999999),random.randint(a=100000,b=999999),random.randint(a=100000,b=999999))
        random.shuffle(self.codes)
        self.nice = code
 
        options = [
            disnake.SelectOption(
                label="Вариант №1", description=self.codes[0], emoji="🔑"
            ),
            disnake.SelectOption(
                label="Вариант №2", description=self.codes[1], emoji="🔑"
            ),
            disnake.SelectOption(
                label="Вариант №3", description=self.codes[2], emoji="🔑"
            ),
            disnake.SelectOption(
                label="Вариант №4",description=self.codes[3],emoji='🔑'
            )
        ]
        super().__init__(
            placeholder="Пройдите капчу...",
            min_values=1,
            max_values=1,
            options=options,
        )
 
 
        async def callback(self,inter: disnake.MessageInteraction):
            if self.values[0] is not self.nice:
                os.remove('temp/verifications/{self.nice}.png')
                embed = disnake.Embed(
                    title='`❌` | Капча не пройдена:',
                    description='Вы не правильно прошли капчу и автоматическая система модерации кикнула вас с сервера, если вы действительно человек, то обратитесь на сервер аппеляций',
                    color=disnake.Color.red()
                )
                await inter.author.send(embed=embed)
            elif self.values[0] is self.nice:
                os.remove('temp/verifications/{self.nice}.png')
                embed = disnake.Embed(
                    title='`✅` | Капча пройдена:',
                    description='Вы прошли проверку и теперь можете получить полный доступ к серверу.',
                    color=disnake.Color.green()
                )
                await inter.author.send(embed=embed)
 
class Verefications(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
 
    @commands.slash_command(name='create')
    async def command_name(self,inter: disnake.CommandInteraction):
        img = ImageCaptcha(width=300,height=300)
        rand = f'{random.randint(a=100000,b=999999)}'
        img.write(rand, f'/temp/verifications/{rand}.png')
        embed = disnake.Embed(
            title='Верификация:',
            description='Для того что бы пройти верефикацию выберите из меню ниже правильный вариант',
            color=disnake.Color.random()
            )
        embed.set_image(file=f'/temp/verifications/{rand}.png')
        inter.send(content=inter.author.mention,embed=embed,view=Verif(code=rand))
 
def setup(bot):
    bot.add_cog(Verefications(bot))