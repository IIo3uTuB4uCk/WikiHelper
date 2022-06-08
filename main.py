import discord
from discord.ui import Button, View
from discord.ext import commands

client = discord.Client()
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="Вики?", intents=intents)
bot.remove_command('help')


@bot.command(name="Зрение")
async def vision(ctx):
    button1 = Button(label="Визуал", emoji="👁", url="https://drive.google.com/file/d/1wRQEDm47bmtaubvu1to9WfbMZ4pO_Xtc/view?usp=sharing")
    button2 = Button(label="Наложение", emoji="👁", url="https://drive.google.com/file/d/1XOGAaUbO32sWxaKkHwugAWixar1w-gwT/view?usp=sharing")
    view = View()
    view.add_item(button1)
    view.add_item(button2)
    await ctx.send("Зрение", view=view)


@bot.command(name="Слух")
async def hearing(ctx):
    button3 = Button(label="Слышимость", emoji="👂", url="https://drive.google.com/file/d/1c_4heYyTlpDB1C01Nh0Akwa5L-TkQmY-/view?usp=sharing")
    button4 = Button(label="Вокализация", emoji="👂", url="https://drive.google.com/file/d/1eMgX8NHo3WYntlZVHvh7sXyCY-aEOYJi/view?usp=sharing")
    view = View()
    view.add_item(button3)
    view.add_item(button4)
    await ctx.send("Слух", view=view)


@bot.command(name="Другие-органы-чувств")
async def other_senses(ctx):
    button5 = Button(label="Обоняние", emoji="👃", url="https://drive.google.com/file/d/1nINF6mvDnvwgKn-5GketEo1rf65w3y5x/view?usp=sharing")
    button6 = Button(label="Вкус", emoji="👄", url="https://drive.google.com/file/d/1eS_RWBy9s7qYrax_BB8Zw6qJRYDaaBzg/view?usp=sharing")
    button7 = Button(label="Тактил", emoji="🤲", url="https://drive.google.com/file/d/1rm1Wi4RJWfpt9ajsRK0UXBTDhZ-Wfu0q/view?usp=sharing")
    button8 = Button(label="ЭП", emoji="👫", url="https://drive.google.com/file/d/1RopVKX1e4MxM9CDjspIaJddKbPcrkllE/view?usp=sharing")
    view = View()
    view.add_item(button5)
    view.add_item(button6)
    view.add_item(button7)
    view.add_item(button8)
    await ctx.send("Другие органы чуств", view=view)


@bot.command(name="Углублённые-практики")
async def deep_practices(ctx):
    button9 = Button(label="Свитч/Позес", emoji="🧍‍♀️", url="https://drive.google.com/file/d/1uzGfN7LpgbZYTVVAg5FcdYk6091VduJq/view?usp=sharing")
    button10 = Button(label="Форсинг во сне", emoji="😴", url="https://drive.google.com/file/d/1EVaTeDtVvea1sON08HWFCPPwGA3awTU2/view?usp=sharing")
    button11 = Button(label="Самофорс", emoji="🧍‍♂️", url="https://drive.google.com/file/d/1Wmehpswd2ARhkkcGbaA85_pzqfrTmhLi/view?usp=sharing")
    view = View()
    view.add_item(button9)
    view.add_item(button10)
    view.add_item(button11)
    await ctx.send("Углублённые практики", view=view)


@bot.command(name="Отклики")
async def signals(ctx):
    button12 = Button(label="Отклики-основное", emoji="💠", url="https://drive.google.com/file/d/15QK7LIWmmy_lHRXHB6jTShjzQNKigb35/view?usp=sharing")
    button13 = Button(label="Мыслеимпульсы", emoji="💠", url="https://drive.google.com/file/d/1li_zjuh2HGClwdOvaimxDQoSimfcFFcg/view?usp=sharing")
    button14 = Button(label="Болевые", emoji="💠", url="https://drive.google.com/file/d/1btIqvLc2yZGGpboch42RU_qVxXUYPyR8/view?usp=sharing")
    button15 = Button(label="Эмоциональные", emoji="💠", url="https://drive.google.com/file/d/1ApPh5g_pF42Ejec9c5aQR_x2WhZWe76I/view?usp=sharing")
    view = View()
    view.add_item(button12)
    view.add_item(button13)
    view.add_item(button14)
    view.add_item(button15)
    await ctx.send("Отклики", view=view)


@bot.command(name="Виды-форсинга")
async def forcing_types(ctx):
    button16 = Button(label="Пассивный форс", emoji="🔰", url="https://drive.google.com/file/d/1-2N8LUUCw9gHhwcZ04dfs3pAM4OwDXZD/view?usp=sharing")
    button17 = Button(label="Активный форс", emoji="🔰", url="https://drive.google.com/file/d/1NKY_ghCMKAh6F_zScc22jRGoGD6uUEx7/view?usp=sharing")
    button18 = Button(label="Активный. В вондере", emoji="🔰", url="https://drive.google.com/file/d/1z27sKkKmdhVWQqwyuSvtBK6D5O9qIce-/view?usp=sharing")
    button19 = Button(label="Активный. Вне вондера", emoji="🔰", url="https://drive.google.com/file/d/1efXneFd2AUJXSe8gLLZYqBh9n4T0nqad/view?usp=sharing")
    view = View()
    view.add_item(button16)
    view.add_item(button17)
    view.add_item(button18)
    view.add_item(button19)
    await ctx.send("Виды форсинга", view=view)


@bot.command(name="Справочник")
async def hand_book(ctx):
    button20 = Button(label="Глоссарий", emoji="📜", url="https://drive.google.com/file/d/1yUyebrHvvyU2kipBfsBZ8qba9_43IAmR/view?usp=sharing")
    button21 = Button(label="Вондер", emoji="⚜", url="https://drive.google.com/file/d/1ApPh5g_pF42Ejec9c5aQR_x2WhZWe76I/view?usp=sharing")
    button22 = Button(label="Фантомные конечности", emoji="👁‍🗨", url="https://drive.google.com/file/d/1ApPh5g_pF42Ejec9c5aQR_x2WhZWe76I/view?usp=sharing")
    button23 = Button(label="Ссылка на сайт", emoji="🌐", url="https://setfisher.wixsite.com/sxema")
    view = View()
    view.add_item(button20)
    view.add_item(button21)
    view.add_item(button22)
    view.add_item(button23)
    await ctx.send("Справочник", view=view)


@bot.command(name="Хелп")
async def help(ctx):
    w1 ="Список команд:"
    w2 = "Префикс: Вики?"
    w3 = "Зрение"
    w4 = "Слух"
    w5 = "Другие-органы-чувств"
    w6 = "Углублённые-практики"
    w7 = "Отклики"
    w8 = "Виды-форсинга"
    w9 = "Справочник"

    s = (w1, w2, w3, w4, w5, w6, w7, w8, w9)
    for i in s:
        await ctx.send(i)
        
bot.run('OTQ1MDA3NjM5NDI1ODU5Njk0.YhJ48g.3M_8XdfHCcHQfUp4RWI6elw-9AI')
