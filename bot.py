from telethon import TelegramClient, events
import datetime
import random

api_id = "####"
mylovec = 1
yourlovec = 1
user = 628040694
api_hash = "######"
client = TelegramClient('my_account', api_id, api_hash)

loveIsMy = [

]
loveIsYour = [

]
love_phrases = [

]

print("Start script")

async def manUserMes(mes, event):
    if mes == "/loveis":
        await event.reply("Від мене: " + random.choice(loveIsMy))
        await event.delete()
        return
    if mes.startswith("/addcomp"):
        loveIsYour.append(mes.replace("/addcomp", "").strip())
        await event.delete()
        return
    for phrase in love_phrases:
        if phrase in mes:
            global yourlovec
            yourlovec += 1

async def manMyMes(mes, event):
    if mes == "/loveis":
        await event.reply("Від Саші\u2764: " + random.choice(loveIsYour))
        await event.delete()
        return
    if mes.startswith("/addcomp"):
        loveIsMy.append(mes.replace("/addcomp", "").strip())
        await event.delete()
        return
    for phrase in love_phrases:
        if phrase in mes:
            global mylovec
            mylovec += 1

async def manBothMes(mes, event):
    if mes == "/stat":
        if (mylovec + yourlovec) > 0:  # Перевірка на нульовий знаменник
            mc = (mylovec / (mylovec + yourlovec)) * 100
        else:
            mc = 0
        await event.reply(f"Любов Саші\u2764: {100 - mc:.2f}% Любов Ростіка: {mc:.2f}%")
        return
    if mes.startswith("/addlove"):
        love_phrases.append(mes.replace("/addlove", "").strip().lower())
        await event.delete()  # Додано видалення повідомлення

@client.on(events.NewMessage)
async def my_event_handler(event):
    try:
        # Перевірка типу peer_id, щоб уникнути помилок
        if event.message.peer_id.user_id == user:
            mes = event.message.message.lower()
            print(mes)

            # Перевірка команди перед викликом manBothMes
            await manBothMes(mes, event)

            # Розрізняємо, хто відправив повідомлення
            if event.sender_id == user:
                print("user")
                await manUserMes(mes, event)
            else:
                print("me")
                await manMyMes(mes, event)

    except Exception as e:
        print(f"Error: {e}")  # Додано вивід помилки для відстеження

client.start()  # запускаємо клієнта
client.run_until_disconnected()  # безкінечний цикл виконання
