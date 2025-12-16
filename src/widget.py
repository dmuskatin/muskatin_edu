from src.masks import mask_account, mask_card


def mask_account_card(acc_number: str) -> str:
    """Возвращет исходную строку с замаскированным номером карты/счета"""

    pay_system = ("Visa", "Maestro", "MasterCard")
    for i in acc_number.split():
        if i in pay_system:
            card_name = " ".join([i for i in acc_number.split() if i.isalpha()])
            card_number = mask_card("".join([i for i in acc_number.split() if i.isdigit()]))
            return f"{card_name + ' ' + card_number}"
        elif i == "Счет":
            account = "".join([i for i in acc_number if i.isdigit()])
            return f"Счет {mask_account(account)}"
    return ''

def get_date(date_and_time: str) -> str:
    """строку с датой в виде дд.мм.гггг"""

    date = [i for i in date_and_time.split("T")]
    return ".".join(list(reversed([i for i in date[0].split("-")])))
