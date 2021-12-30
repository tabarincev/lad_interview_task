import requests

from bs4 import BeautifulSoup


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36',
}


def get_html(url, headers):
    response = requests.get(url, headers=headers)
    return response.text


def get_users_resume_id(url):
    html = get_html(url, headers)
    soup = BeautifulSoup(html, 'html.parser')

    resumes_list = soup.find_all('div', class_='resume-search-item')
    resume_id = []
    
    for i in range(10):
        resume_url = resumes_list[i].find('a', class_='resume-search-item__name')
        ids = resume_url['href'].split('/')[2] 
        sep_ids = ids.split('?')[0]
        resume_id.append(sep_ids)
    
    return resume_id


# Ключевые навыки сотрудника
def get_user_key_skills(html, soup):
    div_class = 'bloko-tag bloko-tag_inline bloko-tag_countable'
    skills = soup.find_all('div', class_=div_class)
    return [skill.get_text() for skill in skills]


clear_sal = lambda sal: eval(sal.replace('\u2009', '').replace('\xa0', '')[:-4])


# Желаемая зарплата сотрудника
def get_user_salary(html, soup):
    span_class = 'resume-block__salary resume-block__title-text_salary'
    salary = soup.find_all('span', class_=span_class)
    return clear_sal(salary[0].text) if salary else None


def get_users_data_json(resumes_id):
    users_json = {}

    for link in resumes_id:
        url_to_parse = 'https://nn.hh.ru/resume/' + link
        html = get_html(url_to_parse, headers)
    
        soup = BeautifulSoup(html, 'html.parser')
    
        key_skills_bs4 = soup.find_all('div', class_='bloko-tag bloko-tag_inline bloko-tag_countable')
        salary = soup.find_all('span', class_='resume-block__salary resume-block__title-text_salary')
        bysyness = soup.find_all('div', class_="resume-block")[0].find_all('p')[0].text.split(':')[1:]
        schedule = soup.find_all('div', class_="resume-block")[0].find_all('p')[1].text.split(':')[1:]
    
        print(url_to_parse)
    
        inner_json = {}
    
        if key_skills_bs4:
            inner_json['Skills'] = [skill.text for skill in key_skills_bs4]
        else:
            inner_json['Skills'] = 'NULL'
        
        if salary:
            inner_json['Salary'] = clear_sal(salary[0].text)
        else:
            inner_json['Salary'] = 'NULL'
    
        if bysyness:
            list_of_bysyness = bysyness[0].split(',')
            list_of_bysyness = [element.strip() for element in list_of_bysyness]
            inner_json['Bysyness'] = list_of_bysyness
    
        if schedule:
            list_of_schedule = schedule[0].split(',')
            list_of_schedule = [element.strip() for element in list_of_schedule]
            inner_json['Schedule'] = list_of_schedule
    
    
        users_json[link] = inner_json
    
    return users_json


resumes_id = get_users_resume_id('https://nn.hh.ru/search/resume?area=113')
users_json = get_users_data_json(resumes_id)