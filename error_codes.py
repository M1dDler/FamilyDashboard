def error_codes (error_code):
    error_dict = {
                   'ERR_INVALID_API_KEY' : 'Помилка API ключа! Негайно повідомте це адміністратору! 👀', 
                   'ERR_TEMPORARY_KEY_NOT_FOUND' :  'Хибний ключ прив’язки. 👀',
                   'ERR_USER_NOT_FOUND' : 'Такого користувача не знайдено в системі. 👀',
                   'ERR_TELEGRAM_ALREADY_LINKED' : 'Веб-профіль вже зв’язано із аккаунтом Telegram! 👀',
                   'ERR_TELEGRAM_USER_NOT_FOUND' : 'Такого користувача не знайдено в системі! 👀'
                 }
    
    default_status = 'Невідома помилка'
    
    return error_dict.get(error_code, default_status)
        