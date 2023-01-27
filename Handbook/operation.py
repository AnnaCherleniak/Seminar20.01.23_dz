def import_data(surname):
    path = 'ДЗ\Seminar20.01.23_dz\Handbook\data.txt'
    with open(path, 'r', encoding='utf-8') as file:
        res_list = []
        while True:
            data = file.readline()
            if not data:
                if not file.readline():
                    break
            if data.rstrip() == surname:
                resuit = []
                resuit.append(surname)
                for _ in range(3):
                    resuit.append(file.readline().rstrip())
                res_list.append(resuit)
        if len(res_list) > 0:
            return res_list
        return 'Данных не найдено.'


def export_data(some_data):
    path = 'ДЗ\Seminar20.01.23_dz\Handbook\data.txt'
    with open(path, 'a', encoding='utf-8') as file:
        file.write('\n')
        for i in range(len(some_data)):
            file.write(f'{some_data[i]}\n')