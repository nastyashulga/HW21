from entity.courier import Courier
from entity.request import Request
from entity.shop import Shop
from entity.store import Store
from exeptions import BaseError

shop = Shop(
    items={
        'печеньки': 3,
        'books': 2,
    },
)
store = Store(
    items={
        'печеньки': 30,
        'books': 20,
    },
)

storages = {
    'магазин': shop,
    'склад': store,
}

def main():
    while True:
        for storage_name in storages:
            print(f'В {storage_name} хранится: {storages[storage_name].get_items()}')

        user_input = input('Введите строку в формате "Доставить 3 печеньки из склад в магазин".\n'
                           'Введите "стоп"/"stop", что бы остановить:\n',
                           )

        if user_input in ('стоп', 'stop'):
            break

        # try:
        request = Request(req_str=user_input, storages=storages)
        # except BaseError as error:
        #     print(error.message)
        #     continue
        # except Exception:
        #    print('неожиданная ошибка')
        #    continue

        courier = Courier(request=request, storages=storages)
        # try:
        courier.move()
        # except BaseException as error:
        #     print(error.message)

if __name__ == '__main__':
    main()