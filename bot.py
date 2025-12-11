import os
import telebot
import random

BOT_TOKEN = os.environ.get("BOT_TOKEN")
if not BOT_TOKEN:
    raise SystemExit("Error: BOT_TOKEN environment variable not set")

bot = telebot.TeleBot(BOT_TOKEN)

rewards = [
    ("You Win 1,000 SHAVEN!", "popup_1000.png"),
    ("You Win 25,000 SHAVEN!", "popup_25000.png"),
    ("You Win 2 USDT!", "popup_2usdt.png"),
    ("You Win 10 USDT!", "popup_10usdt.png"),
    ("You Win 0.1 TON!", "popup_01ton.png"),
    ("You Win 0.5 TON!", "popup_05ton.png"),
    ("You Win 1 TON!", "popup_1ton.png"),
    ("Extra Spin Unlocked!", "popup_extraspin.png"),
]

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "🎉 Welcome to Dobby Dog Spin & Win! Type /spin to play!")

@bot.message_handler(commands=['spin'])
def spin(message):
    reward_text, popup_img = random.choice(rewards)

    try:
        bot.send_photo(message.chat.id, open("wheel.png", "rb"), caption="🎡 Spinning...")
    except:
        bot.send_message(message.chat.id, "🎡 Spinning...")

    try:
        bot.send_photo(message.chat.id, open(popup_img, "rb"), caption=f"🎉 {reward_text}")
    except:
        bot.send_message(message.chat.id, f"🎉 {reward_text}")

bot.polling()
from PIL import Image
import telebot
import time
import os

def send_spinning_animation(bot, chat_id):
    wheel = Image.open("wheel.png")

    frame_paths = []

    # Create 8 rotated frames
    for angle in range(0, 360, 45):
        frame = wheel.rotate(angle, expand=True)
        frame_path = f"frame_{angle}.png"
        frame.save(frame_path)
        frame_paths.append(frame_path)

    # Send frames one-by-one (animation effect)
    for frame in frame_paths:
        bot.send_photo(chat_id, open(frame, "rb"), caption="🎡 Spinning…")
        time.sleep(0.15)  # speed of animation
        bot.delete_message(chat_id, bot.get_updates()[-1].message.message_id)

    # Cleanup frames
    for frame in frame_paths:
        os.remove(frame)
