import os
import random
import time
from datetime import timedelta

from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils import executor

bot = Bot(token='TG-API')
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

skins_folder = 'skins'  # путь к вашей папке со скинами

# клавиатура с кнопками навигации
keyboard_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
start_button = types.KeyboardButton('/start')
skins_button = types.KeyboardButton('/skins')
rolle_button = types.KeyboardButton('/rolle')
keyboard_markup.row(start_button, skins_button, rolle_button)

@dp.message_handler(lambda message: message.text.lower() == '/start')
async def start_command(message: types.Message):
    await message.answer('Благодаря этому боту ты можешь БЕСПЛАТНО получить скин ценой до 5$ Вращая барабан раз в 5 дней!\nЧто бы узнать какие скины в наличии введи "/skins"', reply_markup=keyboard_markup)

@dp.message_handler(lambda message: message.text.lower() == '/skins')
async def show_skins(message: types.Message):
    skins_list = os.listdir(skins_folder)

    for skin in skins_list:
        # создаем полный путь к файлу
        skin_path = os.path.join(skins_folder, skin)

        # убираем расширение из названия файла
        skin_name, _ = os.path.splitext(skin)

        # отправляем изображение скина с именем
        with open(skin_path, 'rb') as skin_image:
            await bot.send_photo(message.chat.id, skin_image, caption=f"Название скина: {skin_name}")

@dp.message_handler(lambda message: message.text.lower() == '/rolle')
async def rolle_skin(message: types.Message):
    last_rolle_data = await storage.get_data(chat=message.chat.id, user=message.from_user.id)
    last_rolle_time = float(last_rolle_data.get('last_rolle_time', 0))

    if time.time() - last_rolle_time > 5 * 24 * 60 * 60:
        # позволяет проходить, если прошло более 5 дней или если это первый раз
        await storage.update_data(chat=message.chat.id, user=message.from_user.id, last_rolle_time=time.time())

        # отправляем эмодзи кубика
        await bot.send_dice(message.chat.id, emoji="🎲")
        time.sleep(5)
        skins_list = os.listdir(skins_folder)
        random_skin = random.choice(skins_list)
        #делаем ссылку на ранд скин
        random_skin_path = os.path.join(skins_folder, random_skin)
        with open(random_skin_path, 'rb') as random_skin_image:
            # увед о выигрыше и т.д.
            await bot.send_photo(message.chat.id, random_skin_image, caption="Поздравляю вы выиграл скин! Подтвердите обмен по ссылке\nFAKE_TRADE_LINK")
    else:
        # вычисляем, сколько времени осталось до следующего использования /rolle
        remaining_time = timedelta(seconds=(5 * 24 * 60 * 60 - (time.time() - last_rolle_time)))
        remaining_time_str = str(remaining_time).split('.')[0]  # удаление милсек
        await message.answer(f"Вы можете использовать команду /rolle только раз в 5 дней. Пожалуйста, подождите еще {remaining_time_str}.")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
