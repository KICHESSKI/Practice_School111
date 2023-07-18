from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher, filters
from aiogram.utils import executor
from loguru import logger
import config
from GglShtTable import GoogleTable
from utils import get_command_number

logger.add(
    config.settings["LOG_FILE"],
    format="{time} {level} {message}",
    level="DEBUG",
    rotation="1 week",
    compression="zip",
)


class Sch111Bot(Bot):
    """Класс информационного бота."""

    def __init__(
            self,
            token: str,
            parse_mode: 'aiogram.enums.ParseMode',
            google_table: GoogleTable = None,
    ) -> None:
        super().__init__(token, parse_mode=parse_mode)
        self._google_table: GoogleTable = google_table


bot: Sch111Bot = Sch111Bot(
    token=config.settings["TOKEN"],
    parse_mode=types.ParseMode.HTML,
    google_table=GoogleTable("creds.json", config.settings['DOC_URL'])
)
dp = Dispatcher(bot)


@dp.message_handler(filters.Regexp(regexp=r"(((П|п)онедельник)(\s)(\d+))"))
async def searchMon(message_from: types.Message) -> None:
    user_id: str = str(message_from.from_id)
    command, number = get_command_number(message_from.md_text)
    values = str(bot._google_table.search_mon(number))
    message = f'{values}\n'
    print(values)
    await message_from.reply(message[2:-3])

@dp.message_handler(filters.Regexp(regexp=r"(((В|в)торник)(\s)(\d+))"))
async def searchTue(message_from: types.Message) -> None:
    user_id: str = str(message_from.from_id)
    command, number = get_command_number(message_from.md_text)
    values = str(bot._google_table.search_tue(number))
    message = f'{values}\n'
    print(values)
    await message_from.reply(message[2:-3])

@dp.message_handler(filters.Regexp(regexp=r"(((С|с)реда)(\s)(\d+))"))
async def searchWen(message_from: types.Message) -> None:
    user_id: str = str(message_from.from_id)
    command, number = get_command_number(message_from.md_text)
    values = str(bot._google_table.search_wen(number))
    message = f'{values}\n'
    print(values)
    await message_from.reply(message[2:-3])


@dp.message_handler(filters.Regexp(regexp=r"(((Ч|ч)етверг)(\s)(\d+))"))
async def searchThur(message_from: types.Message) -> None:
    user_id: str = str(message_from.from_id)
    command, number = get_command_number(message_from.md_text)
    values = str(bot._google_table.search_thur(number))
    message = f'{values}\n'
    print(values)
    await message_from.reply(message[2:-3])

@dp.message_handler(filters.Regexp(regexp=r"(((П|п)ятница)(\s)(\d+))"))
async def searchFri(message_from: types.Message) -> None:
    user_id: str = str(message_from.from_id)
    command, number = get_command_number(message_from.md_text)
    values = str(bot._google_table.search_fri(number))
    message = f'{values}\n'
    print(values)
    await message_from.reply(message[2:-3])

@dp.message_handler(filters.Regexp(regexp=r"(((С|с)уббота)(\s)(\d+))"))
async def searchSat(message_from: types.Message) -> None:
    user_id: str = str(message_from.from_id)
    command, number = get_command_number(message_from.md_text)
    values = str(bot._google_table.search_sat(number))
    if len(values) < 5:
        message = f'выходной'
        await message_from.reply(message)
        print(values)
    else:
        message = f'{values}\n'
        await message_from.reply(message[2:-3])


@dp.message_handler(filters.Regexp(regexp=r"(((П|п)омощь))"))
async def bot_commands_handler(message_from: types.Message) -> None:
    """Обработчик команды Бот."""
    user_id: str = str(message_from.from_id)

    message = (
        f"Привет, я чатбот школы №111)\n\n"
        f" КОМАНДЫ ДЛЯ ЧАТ - БОТА:\n"
        f"❗ Помощь ❗\n"
        f"-- все доступные команды чат-бота 📣\n\n"
        f"❗  Понедельник(№буква) ❗\n"
        f"расписание на понедельник для указанного класса\n\n"
        f"❗  Вторник(№буква) ❗\n"
        f"расписание на вторник для указанного класса\n\n"
        f"❗  Среда(№буква) ❗\n"
        f"расписание на среду для указанного класса\n\n"
        f"❗  Четверг(№буква) ❗\n"
        f"расписание на четверг для указанного класса\n\n"
        f"❗  Пятница(№буква) ❗\n"
        f"расписание на пятницу для указанного класса\n\n"
        f"❗  Суббота(№буква) ❗\n"
        f"расписание на субботу для указанного класса\n\n"
        f"❗  Объявления ❗\n"
        f"свежие новости и объявления школы\n\n"
        f"Все вопросы можно писать с большой и с маленькой буквы, но номер класса всегда слитно!"
    )

    try:
        await message_from.reply(message)
    except Exception as send_error:
        logger.debug(f"{send_error.message}: Trouble id: {user_id}")
        return


@dp.message_handler(filters.Regexp(regexp=r"(((О|о)бъявления))"))
async def News(message_from: types.Message) -> None:
    user_id: str = str(message_from.from_id)

    message = "http://sch111.spb.ru/obyavleniya/#cont"
    message2 = "Объявления находятся по ссылке -> "
    try:
        await message_from.reply(message2 + message)
    except Exception as send_error:
        logger.debug(f"{send_error.message}: Trouble id: {user_id}")
        return


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)