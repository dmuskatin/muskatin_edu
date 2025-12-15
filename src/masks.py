def mask_card(card_number: str) -> str:
    """принимает на  вход номер карты и возвращает ее маску :param card: 1234 56** **** 4356"""

    number = card_number[:6] + len(card_number[6:-4]) * "*" + card_number[-4:]

    lst = []
    for i in range(0, 16, 4):
        lst.append(number[i : i + 4])
    return " ".join(lst)


def mask_account(mask_account: str) -> str:
    """Функция возвращает маску счета"""
    return "*" * 2 + mask_account[-4:]
