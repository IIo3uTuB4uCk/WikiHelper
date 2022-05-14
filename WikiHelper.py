import discord                                                                                              
import credits
import numpy
from discord.ext import commands
from discord_components import DiscordComponents, Button, ButtonStyle

token = credits.bot_token                                                                                   
client = discord.Client()
bot = commands.Bot(command_prefix='Вики?', intents = discord.Intents.all())
bot.remove_command('help')

@bot.event                                                                                                 
async def on_ready():                                                                                        
    DiscordComponents(bot)
    print("Готов к работе")

@bot.command(name = 'Зрение')                                                                                 
async def Зрение(ctx):
    await ctx.send(
        embed = discord.Embed(title = f"WikiHelper",
        description = f"Зрение"),
        components = [Button(style = ButtonStyle.green, label = "Визуал", custom_id="button1"),
                      Button(style = ButtonStyle.green, label = "Наложение", custom_id="button2")])
                
    interaction = await bot.wait_for("button_click", check = lambda i: i.custom_id == "button1") #Визуал
    await interaction.send(content = "https://drive.google.com/file/d/1wRQEDm47bmtaubvu1to9WfbMZ4pO_Xtc/view?usp=sharing")
    
    interaction = await bot.wait_for("button_click", check = lambda i: i.custom_id == "button2") #Наложение
    await interaction.send(content = "https://drive.google.com/file/d/1XOGAaUbO32sWxaKkHwugAWixar1w-gwT/view?usp=sharing")
    
        
@bot.command(name = 'Слух')                                                                                
async def Слух(ctx):
    await ctx.send(
        embed = discord.Embed(title = f"WikiHelper",
        description = f"Слух"),
        components = [Button(style = ButtonStyle.red, label = "Слышимость", custom_id="button3"),
                      Button(style = ButtonStyle.red, label = "Наложение", custom_id="button4")])

    interaction = await bot.wait_for("button_click", check = lambda i: i.custom_id == "button3") #Вокал\Мыслеголос
    await interaction.send(content = "https://drive.google.com/file/d/1c_4heYyTlpDB1C01Nh0Akwa5L-TkQmY-/view?usp=sharing")
    
    interaction = await bot.wait_for("button_click", check = lambda i: i.custom_id == "button4") #Визуал\Наложение
    await interaction.send(content = "https://drive.google.com/file/d/1XOGAaUbO32sWxaKkHwugAWixar1w-gwT/view?usp=sharing")
    
@bot.command(name = 'ДругиеОрганыЧувств')                                                                                
async def ДругиеОрганыЧувств(ctx):
    await ctx.send(
        embed = discord.Embed(title = f"WikiHelper",
        description = f"Другие органы чувств"),
        components = [Button(style = ButtonStyle.blue, label = "Обоняние", custom_id="button5"),
                      Button(style = ButtonStyle.blue, label = "Вкус", custom_id="button6"),
                      Button(style = ButtonStyle.blue, label = "Тактил", custom_id="button7"),
                      Button(style = ButtonStyle.blue, label = "ЭП", custom_id="button8")])

    interaction = await bot.wait_for("button_click", check = lambda i: i.custom_id == "button5") #Обоняние
    await interaction.send(content = "https://drive.google.com/file/d/1ApPh5g_pF42Ejec9c5aQR_x2WhZWe76I/view?usp=sharing")
    
    interaction = await bot.wait_for("button_click", check = lambda i: i.custom_id == "button6") #Вкус
    await interaction.send(content = "https://drive.google.com/file/d/1eS_RWBy9s7qYrax_BB8Zw6qJRYDaaBzg/view?usp=sharing")
    
    interaction = await bot.wait_for("button_click", check = lambda i: i.custom_id == "button7") #Тактил
    await interaction.send(content = "https://drive.google.com/file/d/1rm1Wi4RJWfpt9ajsRK0UXBTDhZ-Wfu0q/view?usp=sharing")
    
    interaction = await bot.wait_for("button_click", check = lambda i: i.custom_id == "button8") #Визуал\Наложение
    await interaction.send(content = "https://drive.google.com/file/d/1RopVKX1e4MxM9CDjspIaJddKbPcrkllE/view?usp=sharing")
    
@bot.command(name = 'Углублённые_практики')                                                                                
async def Углублённые_практики(ctx):
    await ctx.send(
        embed = discord.Embed(title = f"WikiHelper",
        description = f"Углублённые практики"),
        components = [Button(style = ButtonStyle.grey, label = "Свич\Позес", custom_id="button9"),
                      Button(style = ButtonStyle.grey, label = "Форсинг во сне", custom_id="button10"),
                      Button(style = ButtonStyle.grey, label = "Самофорс", custom_id="button11")])

    interaction = await bot.wait_for("button_click", check = lambda i: i.custom_id == "button9") #Вокал\Мыслеголос
    await interaction.send(content = "https://drive.google.com/file/d/1uzGfN7LpgbZYTVVAg5FcdYk6091VduJq/view?usp=sharing")
    
    interaction = await bot.wait_for("button_click", check = lambda i: i.custom_id == "button10") #Форсинг во сне
    await interaction.send(content = "https://drive.google.com/file/d/1ApPh5g_pF42Ejec9c5aQR_x2WhZWe76I/view?usp=sharing")
    
    interaction = await bot.wait_for("button_click", check = lambda i: i.custom_id == "button11") #Самофорс
    await interaction.send(content = "https://drive.google.com/file/d/1Wmehpswd2ARhkkcGbaA85_pzqfrTmhLi/view?usp=sharing")
    
@bot.command(name = 'Отклики')                                                                                
async def Отклики(ctx):
    await ctx.send(
        embed = discord.Embed(title = f"WikiHelper",
        description = f"Отклики"),
        components = [Button(style = ButtonStyle.green, label = "Отклики основное", custom_id="button12"),
                      Button(style = ButtonStyle.green, label = "Мыслеимпульсы", custom_id="button13"),
                      Button(style = ButtonStyle.green, label = "Болевые", custom_id="button14"),
                      Button(style = ButtonStyle.green, label = "Эмоциональные", custom_id="button15")])

    interaction = await bot.wait_for("button_click", check = lambda i: i.custom_id == "button12") #Отклики Основное
    await interaction.send(content = "https://drive.google.com/file/d/15QK7LIWmmy_lHRXHB6jTShjzQNKigb35/view?usp=sharing")
    
    interaction = await bot.wait_for("button_click", check = lambda i: i.custom_id == "button13") #Мыслеимпульсы
    await interaction.send(content = "https://drive.google.com/file/d/1ApPh5g_pF42Ejec9c5aQR_x2WhZWe76I/view?usp=sharing")
    
    interaction = await bot.wait_for("button_click", check = lambda i: i.custom_id == "button14") #Болевые
    await interaction.send(content = "https://drive.google.com/file/d/1ApPh5g_pF42Ejec9c5aQR_x2WhZWe76I/view?usp=sharing")
    
    interaction = await bot.wait_for("button_click", check = lambda i: i.custom_id == "button15") #Эмоциональные
    await interaction.send(content = "https://drive.google.com/file/d/1ApPh5g_pF42Ejec9c5aQR_x2WhZWe76I/view?usp=sharing")
    
@bot.command(name = 'Виды_форсинга')                                                                                
async def Виды_форсинга(ctx):
    await ctx.send(
        embed = discord.Embed(title = f"WikiHelper",
        description = f"Виды_форсинга"),
        components = [Button(style = ButtonStyle.red, label = "Пассивный", custom_id="button16"),
                      Button(style = ButtonStyle.red, label = "Активный", custom_id="button17"),
                      Button(style = ButtonStyle.red, label = "Активный(Вондер)", custom_id="button18"),
                      Button(style = ButtonStyle.red, label = "Активный(Вне вондера)", custom_id="button19")])

    interaction = await bot.wait_for("button_click", check = lambda i: i.custom_id == "button16") #Пассивный
    await interaction.send(content = "https://drive.google.com/file/d/1-2N8LUUCw9gHhwcZ04dfs3pAM4OwDXZD/view?usp=sharing")
    
    interaction = await bot.wait_for("button_click", check = lambda i: i.custom_id == "button17") #Активный
    await interaction.send(content = "https://drive.google.com/file/d/1NKY_ghCMKAh6F_zScc22jRGoGD6uUEx7/view?usp=sharing")
    
    interaction = await bot.wait_for("button_click", check = lambda i: i.custom_id == "button18")#Активный(Вондер)
    await interaction.send(content = "https://drive.google.com/file/d/1z27sKkKmdhVWQqwyuSvtBK6D5O9qIce-/view?usp=sharing")
    
    interaction = await bot.wait_for("button_click", check = lambda i: i.custom_id == "button19") #Активный(Вне вондера)
    await interaction.send(content = "https://drive.google.com/file/d/1efXneFd2AUJXSe8gLLZYqBh9n4T0nqad/view?usp=sharing")

@bot.command(name = 'Справочник')                                                                                
async def Справочник(ctx):
    await ctx.send(
        embed = discord.Embed(title = f"WikiHelper",
        description = f"Справочник"),
        components = [Button(style = ButtonStyle.blue, label = "Глоссарий", custom_id="button20"),
                      Button(style = ButtonStyle.blue, label = "Вондер", custom_id="button21"),
                      Button(style = ButtonStyle.blue, label = "Фантомные конечности", custom_id="button22"),
                      Button(style = ButtonStyle.blue, label = "Полная версия", custom_id="button23")])

    interaction = await bot.wait_for("button_click", check = lambda i: i.custom_id == "button16") #Глоссарий
    await interaction.send(content = "https://drive.google.com/file/d/1yUyebrHvvyU2kipBfsBZ8qba9_43IAmR/view?usp=sharing")
    
    interaction = await bot.wait_for("button_click", check = lambda i: i.custom_id == "button17") #Вондерленд
    await interaction.send(content = "https://drive.google.com/file/d/1ApPh5g_pF42Ejec9c5aQR_x2WhZWe76I/view?usp=sharing")
    
    interaction = await bot.wait_for("button_click", check = lambda i: i.custom_id == "button18") #Мыслеформные конечности
    await interaction.send(content = "https://drive.google.com/file/d/1ApPh5g_pF42Ejec9c5aQR_x2WhZWe76I/view?usp=sharing")
    
    interaction = await bot.wait_for("button_click", check = lambda i: i.custom_id == "button19") #Визуал\Наложение
    await interaction.send(content = "https://setfisher.wixsite.com/sxema")
    
@bot.command(name = 'Хелп')                                                                                
async def Хелп(ctx):
    await ctx.send("```Список команд:```"
                   "```Префикс: Вики?```"
                   "```Зрение```"
                   "```Слух```"
                   "```ДругиеОрганыЧувств```"
                   "```Углублённые_практики```"
                   "```Отклики```"
                   "```Виды_форсинга```"
                   "```Справочник```")

vector = numpy.vectorize(Зрение)
vector = numpy.vectorize(Слух)
vector = numpy.vectorize(ДругиеОрганыЧувств)
vector = numpy.vectorize(Углублённые_практики)
vector = numpy.vectorize(Отклики)
vector = numpy.vectorize(Виды_форсинга)
vector = numpy.vectorize(Справочник)


bot.run(token)