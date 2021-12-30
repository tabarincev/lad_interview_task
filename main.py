import config

from parser import users_json, resumes_id
from database import Database


config_db = {
    'user': config.username,
    'password': config.db_passwd,
    'host': config.db_host,
    'port': config.db_port,
    'dbname': config.db_name,
}

db = Database(**config_db)


for i in range(len(resumes_id)):
    user_resume_id = resumes_id[i]
    salary = users_json[user_resume_id]['Salary']
    user_skills = users_json[user_resume_id]['Skills']
    user_bysyness = users_json[user_resume_id]['Bysyness']
    user_schedule = users_json[user_resume_id]['Schedule']

    to_tuple_str = lambda n: n.replace('[', '(').replace(']', ')')

    # вставка в таблицу 'users'
    add_resume_salary = """
        INSERT INTO users 
        (resume_id, salary)
        VALUES ('{0}', {1})""".format(user_resume_id, salary)

    db.insert_into_table(add_resume_salary)

    # вставка в таблицу 'skills'
    for skill in user_skills:
        insert_skills = """
            INSERT INTO skills 
            (skill_name) 
            VALUES ('{0}')""".format(skill)

        db.insert_into_table(insert_skills)

    # вставка в таблицу 'user-skills'
    tuple_user_skills = to_tuple_str(str(user_skills))
    
    insert_user_skills = """
        INSERT INTO user_skills 
        (resume_id, skill_id)
        SELECT '{0}', skill_id FROM skills 
        WHERE skill_name IN {1}""".format(user_resume_id, 
                                          tuple_user_skills)

    db.insert_into_table(insert_user_skills)

    # вставка в таблицу 'bysyness'
    
    for bysyness in user_bysyness:
        insert_bysyness = """
            INSERT INTO bysyness
            (bysyness_name) 
            VALUES ('{0}')""".format(bysyness)

        db.insert_into_table(insert_bysyness)

    # вставка в таблицу 'user-bysyness'
    tuple_user_bysyness = to_tuple_str(str(user_bysyness))

    insert_user_bysyness = """
        INSERT INTO user_bysyness 
        (resume_id, bysyness_id)
        SELECT '{0}', bysyness_id FROM bysyness
        WHERE bysyness_name IN {1}""".format(user_resume_id, 
                                             tuple_user_bysyness)

    db.insert_into_table(insert_user_bysyness)

    # вставка в таблицу 'schedule'
    for schedule in user_schedule:
        insert_schedule = """
            INSERT INTO schedule
            (schedule_name) 
            VALUES ('{0}')""".format(schedule)

        db.insert_into_table(insert_schedule)
    
    # вставка в таблицу 'user-schedule'
    tuple_user_schedule = to_tuple_str(str(user_schedule))

    insert_user_schedule = """
        INSERT INTO user_schedule
        (resume_id, schedule_id)
        SELECT '{0}', schedule_id FROM schedule
        WHERE schedule_name IN {1}""" .format(user_resume_id,
                                              tuple_user_schedule)

    db.insert_into_table(insert_user_schedule)

