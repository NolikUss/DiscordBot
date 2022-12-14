import asyncio
import disnake
from disnake.ext import commands
import sqlite3

connection = sqlite3.connect('customrooms.db')
cursor = connection.cursor()

def create_db():
    cursor.execute("""CREATE TABLE IF NOT EXISTS voice_rooms (
        owner BIGINT,
        room_id BIGINT
    );""")
    connection.commit()

def create_room(owner,room_id):
    my_list = (owner,room_id)
    cursor.execute("""INSERT INTO voice_rooms VALUES (?,?);""",my_list)

class TextRooms(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot


    @commands.slash_command(name='temp-room',description='Создаёт личную текстовую комнату которая действует 24 часа')
    async def temp_room(self,inter: disnake.CommandInteraction):
        channel = await inter.guild.create_text_channel(name='TEMP-{}'.format(inter.author.display_name))
        await inter.send(channel.mention)
        perms = channel.permissions_for(inter.author)
        perms.send_messages = True
        perms.stream = True
        perms.manage_channels = True
        perms.mute_members = True
        perms.moderate_members = True
        create_room(owner=inter.author.id,room_id=1)


def setup(bot):
    bot.add_cog(TextRooms(bot))
