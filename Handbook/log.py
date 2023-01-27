from datetime import datetime

def log_cash(mod, result):
    path = 'ДЗ\Seminar20.01.23_dz\Handbook\log.txt'
    with open(path, 'a', encoding='utf-8') as file:
        file.write(f'Время запроса: {datetime.now()}; Вид запроса: {mod}; Данные: {result}\n')
