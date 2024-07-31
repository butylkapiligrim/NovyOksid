import logging

from src.logger import setup_logging

logger = setup_logging()


def account_mask(num_account: str) -> str:
    "Легендарно берет номер счета и делает его под маской"
    mask_account = num_account[-4:]
    logger.info("Функция account_mask выполнена успешно")  # Используем masks_logger
    return f"**{mask_account}"


def card_mask(cards_mask: str) -> str:
    "Эпически берет номер карты и делает его под маской"
    mask_card = f"{cards_mask[:4]} {cards_mask[4:6]}** **** {cards_mask [-4:]}"
    logger.info("Функция card_mask выполнена успешно")
    return mask_card


# ⢀⢀⣠⣶⡶⠾⠿⠶⣶⣶⣤⣤⣤⠀⠀⠀⠀⢠⣤⣤⣴⣶⣶⣾⠿⠷⢶⣮⣖⠄
# ⠁⠛⠁⠀⠀⠀⠤⠤⠤⠤⠤⠉⠁⠀⠀⠀⠀⠀⠈⠉⠀⠀⠀⠀⠄⠀⠀⠀⠉⠓
# ⠀⠀⠀⠀⠊⢹⣿⣿⣿⠙⡆⠀⠳⠀⠀⠀⠀⠀⠇⠀⡼⠋⣿⣿⣿⠉⠑⠄⠀⠀
# ⠀⠀⠀⠈⠉⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠉⠉⠀⠀⠀ ⠀⠀⠀
#    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠂⠀
# ⠀⠀   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⢠⠃⠀⠀
# ⠀  ⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⡤⠴⠚⠁⠀⠀⡎⠀⠀⠀
# ⠀⠀⠀⠀⠀⠙⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠰⠀
