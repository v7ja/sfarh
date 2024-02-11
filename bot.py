from OpsAi import Ai
from pyrogram import Client,filters

app = Client("ChatGpt", api_id=27435520,api_hash="3206293f0d15e0a23ed0cb198e19aab8",bot_token="6762979530:AAG5DMNhpKxJC7ITbrPd-1qI-QzF4k7su4w") 


@app.on_message(filters.command("start"))
async def StartMsg(_,msg):
 await msg.reply("Hello iam Chat Gbt Bot")

@app.on_message()
async def echo(bot, msg):
    a = msg.text
    s = Ai(query = a)
    await bot.send_message(chat_id=msg.chat.id, text=s.chat())    
    
app.run()
