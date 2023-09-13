import os

from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from dotenv import load_dotenv

from google_handler import save_data


load_dotenv()
API_TOKEN = os.getenv('TELEGRAM_TOKEN')
PRIVATE_GROUP_LINK = os.getenv('TELEGRAM_GROUP_LINK')


bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())


class Form(StatesGroup):
    fullname = State()
    phone = State()
    email = State()
    social_media = State()
    profession = State()
    help = State()


@dp.message_handler(commands=['start'], state='*')
async def start(message: types.Message) -> None:
    await bot.send_message(message.chat.id, 'Привет!\nОтветь на несколько вопросов, чтобы попасть в группу.\nНажми на 👉🏻 /nachat_opros.')


@dp.message_handler(commands=['nachat_opros'])
async def start_poll(message: types.Message) -> None:
    await bot.send_message(message.chat.id, 'Как вас зовут?')
    await Form.fullname.set()


@dp.message_handler(state=Form.fullname)
async def process_fullname(message: types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        data['fullname'] = message.text
    await bot.send_message(message.chat.id, "Ваш номер телефона:")
    await Form.next()


@dp.message_handler(state=Form.phone)
async def process_phone(message: types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        data['phone'] = message.text
    await bot.send_message(message.chat.id, "Ваш E-mail:")
    await Form.next()


@dp.message_handler(state=Form.email)
async def process_email(message: types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        data['email'] = message.text
    await bot.send_message(message.chat.id, "Ссылка на ваши социальные сети:")
    await Form.next()


@dp.message_handler(state=Form.social_media)
async def process_social_media(message: types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        data['social_media'] = message.text
    await bot.send_message(message.chat.id, "Какая у вас профессия?")
    await Form.next()


@dp.message_handler(state=Form.profession)
async def process_profession(message: types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        data['profession'] = message.text
    await bot.send_message(message.chat.id, "Чем бы вы хотели помогать людям?")
    await Form.next()


@dp.message_handler(state=Form.help)
async def process_help(message: types.Message, state: FSMContext) -> None:
    await bot.send_message(message.chat.id, f"Спасибо за участие в опросе! Чтобы вступить в группу перейдите по ссылке: {PRIVATE_GROUP_LINK}")
    async with state.proxy() as data:
        data['help'] = message.text
    save_data(dict(data))
    await state.finish()


if __name__ == '__main__':
    from aiogram import executor

    executor.start_polling(dp, skip_updates=True)
