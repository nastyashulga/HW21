class BaseError(Exception):
    message = 'Неизвестная ошибка'

class NotEnoughSpaceError(BaseError):
   massage = 'Недостаточно места'

class NotEnoughProductError(BaseError):
   massage = 'Недостаточно товара'

class UnknownProductError(BaseError):
    massage = 'Неизвестный товар'

class InvalidRequestError(BaseError):
    massage = 'Неправильный запрос'

class UnknownStorageError(BaseError):
    massage = 'Неизвестный склад'

class TooManyDifferentProductsError(BaseError):
    massage = 'Слишком много разных товаров'

