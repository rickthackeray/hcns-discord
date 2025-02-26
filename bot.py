import discord
from discord.ext import commands
from discord import app_commands

from keys import BOT_TOKEN

CHANNEL_ID = 1338670037799796858

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("HEEEEELLOO BOT READY")
    channel = bot.get_channel(CHANNEL_ID)
    view = discord.ui.View()
    shipbutton = discord.ui.Button(label="New Ship Order", emoji="⚓")
    repairbutton = discord.ui.Button(label="Repair and/or Rearm Request", emoji="🛠️")

    boat_view = discord.ui.View()
    boat_select = discord.ui.Select(
        placeholder="Select the ship you want to order",
        options=[
            discord.SelectOption(label="Longhook - 640rm", value="longhook"),
            discord.SelectOption(label="Bowhead - 640rm", value="bowhead"),
            discord.SelectOption(label="Submarine (Nakki) - 960rm", value="sub"),
            discord.SelectOption(label="Frigate (Blacksteele) - 1200rm", value="frig"),
            discord.SelectOption(label="Bluefin - 2000rm", value="bluefin"),
            discord.SelectOption(label="Battleship (Callahan) - 3200rm + 80am5", value="bs"),
        ]
    )
    boat_view.add_item(boat_select)
    boat_contacts = discord.ui.

    async def button_callback(interaction):
        await interaction.user.send("Please fill the form below to open a new ship order.", view=boat_view)

    shipbutton.callback = button_callback

    view.add_item(shipbutton)
    view.add_item(repairbutton)

    response = await channel.create_thread(name="START HERE!",view=view)
    thread_id = response.thread.id



    try:
        synced_commands = await bot.tree.sync()
        print(f"Synced {len(synced_commands)} commands")
    except Exception as error:
        print("command sync error: ", error)

    



@bot.command()
async def add_rares(context, amount):
    await context.send(f"I would add {amount} rare metals to the total if I knew the total!")


#@bot.tree.command(name="boatorder", description="Start a new order for a ship")
@bot.command()
async def boatorder(context):
    boat_view = discord.ui.View()
    select = discord.ui.Select(
        placeholder="Select the ship you want to order",
        options=[
            discord.SelectOption(label="Longhook - 640rm", value="longhook"),
            discord.SelectOption(label="Bowhead - 640rm", value="bowhead"),
            discord.SelectOption(label="Submarine (Nakki) - 960rm", value="sub"),
            discord.SelectOption(label="Frigate (Blacksteele) - 1200rm", value="frig"),
            discord.SelectOption(label="Bluefin - 2000rm", value="bluefin"),
            discord.SelectOption(label="Battleship (Callahan) - 3200rm + 80am5", value="bs"),
            
        ]
    )
    boat_view.add_item(select)
    await context.send(view=boat_view)





# @bot.command()
# async def newpost(context):
#     channel = bot.get_channel(1338670037799796858)
#     await channel.create_thread(name="thread test", content="content here")

# class OrderForm(discord.ui.Modal, title="New Ship Order"):
#     regiment = discord.ui.TextInput(label="Regiment:", style=discord.TextStyle.short, placeholder="Enter your regiment or username if solo")
#     ship = discord.ui.TextInput(label="Ship:", style=discord.TextStyle.short)

#     async def on_submit(self, interaction: discord.Interaction):
#         # can do input validation here
#         await interaction.response.send_message("Order created!")

# @bot.tree.command(name="order", description="New order")
# async def order(interaction: discord.Interaction):
#     modal = OrderForm()
#     modal.user = interaction.user
#     await interaction.response.send_modal(modal)

bot.run(BOT_TOKEN)
