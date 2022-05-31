import requests
from bs4 import BeautifulSoup

class Bomber:
    '''Help to bomb one-list GForms without autorization'''
    def __init__(self, link, mail) -> None:
        '''`link` is a link to form with "viewform" on close'''
        self.link = link
        self.url = self.link.replace('viewform', '').replace('formResponse', '') + 'formResponse'
        self.mail = mail

    def start(self, num_of_requests:int, answers:list, question_seq:list[int]=None, print_result=False):
        '''Start bombing\n
           `answers` :list[any]:\n
           `question_seq` :list[int] | int: is sequence of questions to answer.'''
        def sorting(x):
            x = x['data-params'][x['data-params'].index(',[[') + 3:]
            return x[:x.index(',')]
        req_list = []
        try:
            response = requests.get(self.link)
        except requests.exceptions.ConnectionError as error:
            print(f'You have some troubles with internet connection, try later\n{error}')
            return error
        soup = BeautifulSoup(response.text, 'lxml')
        params = list(map(sorting, soup.find_all('div', jsmodel = "CP1oW")))
        for i in range(num_of_requests):
            form_data = {
                        'draftResponse':[],
                        'pageHistory':0}
            if question_seq is not None:
                for j, v in enumerate(question_seq):
                    form_data['entry.' + params[v]] = answers[j]
            else:
                for j, v in enumerate(params):
                    form_data['entry.' + v] = answers[j]
            user_agent = {'Referer': self.link,'User-Agent': "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.52 Safari/537.36"}
            r = requests.post(self.url, data=form_data, headers=user_agent)
            req_list.append(r.status_code)
            if print_result:
                print(f'{i + 1} / {num_of_requests} - {"Sucsessful" if r.status_code == 200 else f"Failed: {r.status_code}"}')
        return req_list


if __name__ == '__main__':
    bber = Bomber('https://docs.google.com/forms/d/e/1FAIpQLSe9Nf5RATGkcd01JAjWRVqMY0dqrhOMoODewsd6E16p5d3r9g/viewform', 'boss.trushchelev@mail.ru')
    bber.start(10, ['answer1', [2, 4], 3], print_result=True)
