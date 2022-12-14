import disnake
from disnake.ext import commands
from config import setting



class Button(disnake.ui.View):
    def __init__(bot,self,member: disnake.Member, timeout=0):
        self.bot = bot
        self.member = member
        super().__init__(timeout=timeout)

    @disnake.ui.button(label='Ответить',style=disnake.ButtonStyle.green,emoji='🔩')
    async def callback(self, button: disnake.ui.Button, inter: disnake.MessageInteraction):
        await inter.send('Пожалуйста ниже отправьте сообщение которое нужно отправить пользователю')
        message = self.bot.wait_for('message')
        await self.member.send(message)
            


class OnMessage(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_message(self,message: disnake.MessageInteraction):
        if message.author.id == setting['botid']:
            pass
        elif message.guild == None:
            embed = disnake.Embed(
                title='`🐉` | Боту было отправлено личное сообщение',
                description='Информация будет приложена ниже',
                color=disnake.Color.blue()
            )
            embed.set_author(icon_url=message.author.avatar.url,name=message.author.name)
            embed.add_field(name='Текст этого сообщения:',value=message.content)
            channel = self.bot.get_channel(1052518969371799582)
            await channel.send(embed=embed,view=Button(bot=self.bot,member=message.author))
        
def setup(bot):
    bot.add_cog(OnMessage(bot))
