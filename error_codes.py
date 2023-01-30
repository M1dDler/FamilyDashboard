def error_codes (error_code):
    error_dict = {
                   'ERR_THE_KEY_HAS_EXPIRED' : 'Ключ не дійсний', 
                    'ERR_NOT_FOUND_KEY' : 'Ключ не найдено',
                    'ERR_TELEGRAM_ALREADY_LINKED' : 'До веб-профілю за цим посиланням вже прив’язано аккаунт Telegram 👀',
                    'ERR_NOT_FOUND_USER' : 'Помилка, не знайдено користувача в системі 👀'
                 }
    
    default_status = 'Невідома помилка'
    
    return error_dict.get(error_code, default_status)
        