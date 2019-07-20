#!/usr/bin/env python3

import psycopg2

question1 = '''
1. What are the most popular three articles of all time?
'''
question1_query = '''
    select articles.title, COUNT(*) as views
    from articles 
    join log on log.path like CONCAT('%',articles.slug)
    group by title
    order by views desc
    limit 3
    '''
    
question2 = '''
2. Who are the most popular article authors of all time?
'''
question2_query = '''
    select authors.name, COUNT(*) as views
    from authors
    join articles on authors.id = articles.author
    join log on log.path like CONCAT('%',articles.slug)
    group by authors.name
    order by views desc
    '''


question3 = '''
3. On which days did more than 1 percent of requests lead to errors?
'''
question3_query = '''
    select TO_CHAR(error.d,'MON-DD-YYYY') as date ,
            ROUND((error.c::decimal*100/total.c),3) as p 
    from (select DATE(time) as d, COUNT(*) as c 
        from log 
        where status like '4%' 
        group by d) as error 
    join (select DATE(time) as d, COUNT(*) as c 
        from log group by d) as total 
    on error.d = total.d
    where (error.c::decimal*100/total.c) >= 1
    '''


def query_news(query):
    db = psycopg2.connect(dbname='news')
    c = db.cursor()
    c.execute(query)
    results = c.fetchall()
    db.close()
    return results

def print_result(results, append):
     [print(str(r[0])+' -- '+str(r[1])+append) for  r in results]
     print()
    

if __name__ == '__main__':
    print(question1)
    print_result(query_news(question1_query)," views")
    
    print(question2)
    print_result(query_news(question2_query)," views")
    
    print(question3)
    print_result(query_news(question3_query),"% Erros")