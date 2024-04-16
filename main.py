!pip install aiogram
import aiogram
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder
import asyncio

from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

API_TOKEN = '7112549885:AAH5uICZ8Yk2AI9zg4YamhrsxFdHp2QNQ6I'
BOT = Bot(token=API_TOKEN)
DP = Dispatcher()

class States(StatesGroup):
  STATE_register = State()
  STATE_last_name = State()

USER_DICT = {}

@DP.message(Command('register'))
async def cmd_register(message: types.Message, state: FSMContext):
  await state.set_state(States.STATE_register)
  await message.answer('Как ваше имя?')


@DP.message(States.STATE_register)
async def register(message: types.Message, state: FSMContext):
  user_id = message.from_user.id
  if user_id not in USER_DICT:
    USER_DICT[user_id] = {}
  USER_DICT[user_id]['name'] = message.text
  await message.answer('Как ваша фамилия?')
  await state.set_state(States.STATE_last_name)


@DP.message(States.STATE_last_name)
async def last_name(message: types.Message, state: FSMContext):
  user_id = message.from_user.id
  USER_DICT[user_id]['last_name'] = message.text
  await message.answer('Кто вы по знаку зодиака?')
