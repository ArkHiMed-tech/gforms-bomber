import random

import requests

inp = input('Введите ссылку на форму: ')
inp = inp.replace('viewform', '')
url = inp + 'formResponse'
 
count = int(input('Введите количество голосов: '))
mail = input('Введите почту: ')
 
for i in range(count):
    form_data = {'entry.986720168': ''.join(random.choices(list('1234567890'), k=1)),
                 'entry.1704626263': random.sample(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'], k=random.randint(1, 10)),
                 'entry.1679341224': random.choice([1, 2, 3, 4]),
                 'entry.1358430264': mail,
                'draftResponse':[],
                'pageHistory':0}
    user_agent = {'Referer': inp + 'viewform','User-Agent': "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.52 Safari/537.36"}
    r = requests.post(url, data=form_data, headers=user_agent)
    print(r.status_code)
