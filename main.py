from src.masks import mask_card, mask_account
from src.processing import filter_by_state, sort_by_date
from src.widget import mask_account_card, get_date

if __name__ == '__main__':
    list_ = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
             {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
             {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
             {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
    print(filter_by_state(list_))
    print(filter_by_state(list_, 'CANCELED'))
    print(sort_by_date(list_))
    print(sort_by_date(list_, True))
    print(mask_account_card("Visa Platinum 7000 7922 8960 6361"))
    print(mask_account_card("Счет 73654108430135874305"))
    print(get_date("2018-07-11T02:26:18.671407"))
    print(mask_card("1234567891234356"))
    print(mask_account("73654108430135874305"))