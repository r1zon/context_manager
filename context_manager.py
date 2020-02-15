import datetime

import requests

class my_open:

    def __init__(self, path):
        self.path = path
        self.start_time = datetime.datetime.now()
        print(f'Время начала программы: {self.start_time}')


    def __enter__(self):
        self.file = open(self.path)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end_time = datetime.datetime.now()
        self.delay_time = self.end_time - self.start_time
        print(f'Программа завершилась в: {self.end_time}')
        print(f'Время выполнения программы: {self.delay_time}\n')
        self.file.close()

def main():
    print('*'*20)
    print('Условие')
    print('*'*20)
    print('Имеется набор файлов, каждый из которых, кроме последнего, содержит имя следующего файла. \n'
          'Первое слово в тексте последнего файла: "We".\n'
          'В документе doc_context содержится ссылка на первый файл из этого набора.\n'
          'Программа находит последний файл и выводит его текст. \n'
          'Внимание! Время выполнения может занимать более минуты.')
    print('*'*20)
    while True:
        next_step = input('Нажмите c, чтобы запустить программу. '
                          'Для выхода нажмите q.\n')
        if next_step == 'c':
            if __name__ == '__main__':
                with my_open('doc_context.txt') as file:
                    line = file.readline().strip()
                    doc_text = requests.get(line)
                    url = 'https://stepic.org/media/attachments/course67/3.6.3/'
                    new_url = url + str(doc_text.text)
                    count_requests = 0
                    while 'We ' not in new_url:
                        text = requests.get(new_url)
                        new_url = url + str(text.text)
                        count_requests += 1
                    print('*'*20)
                    print(f'Текст файла: \n'
                          f'{text.text}')
                    print('*'*20)
                    print(f'Номер последнего файла: {count_requests}')
        elif next_step == 'q':
            break
main()