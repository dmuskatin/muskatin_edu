def filter_by_state(transactions: list[dict], state: str = "EXECUTED") -> list[dict]:
    """сортировка по ключу 'state'"""
    res_list = []
    for transaction in transactions:
        if transaction.get("state") == state:
            res_list.append(transaction)
    return res_list


def sort_by_date(transactions: list[dict], sort: bool = False) -> list[dict]:
    """сортировка по дате"""
    return sorted(transactions, key=lambda x: x["date"], reverse=sort)
