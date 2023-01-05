from google.cloud import bigquery


# 2. How many articles did the New York Times write about 
# China in July 2016? What about July 2017? 
# /////////////////////////////////////////////////////////////
# July 2016
# RUN : 1 row in set (7 min 53.19 sec)
query2_1 = '''select count(*) from gdelt-bq.gdeltv2.eventmentions m 
              inner join gdelt-bq.gdeltv2.events e on e.GLOBALEVENTID=m.GLOBALEVENTID 
              where m.MentionSourceName LIKE '%nytimes.com%' 
              and e.MonthYear=201607 
              and (Actor1Geo_CountryCode= 'US' or Actor2Geo_CountryCode= 'US') 
              and ActionGeo_CountryCode='US';'''
# July 2017
query2_2 = '''select count(*) from gdelt-bq.gdeltv2.eventmentions m 
              inner join gdelt-bq.gdeltv2.events e on e.GLOBALEVENTID=m.GLOBALEVENTID 
              where m.MentionSourceName LIKE '%nytimes.com%' 
              and e.MonthYear=201707 
              and (Actor1Geo_CountryCode= 'US' or Actor2Geo_CountryCode= 'US') 
              and ActionGeo_CountryCode='US';'''

# 6.Top 30 most important articles that happened in the US about 
# specific areas, for example China? What is the average tone 
# and importance in the impact of these articles? 
# /////////////////////////////////////////////////////////////
# RUN : 30 rows in set (3 min 5.69 sec) 
query6_1 = ''' select GoldsteinScale, Avgtone, NumMentions from gdelt-bq.gdeltv2.events 
               where (Actor1Geo_CountryCode='CH' or Actor2Geo_CountryCode='CH')
               and ActionGeo_CountryCode='US'  
               order by NumMentions desc limit 30;'''


# 10.Get the quadclass and GoldsteinScale of events occuring in China specifically Hong Kong. 
# *Note: Will expand upon this further
# /////////////////////////////////////////////////////////////
# RUN : 53141 rows in set (3 min 45.74 sec)
query10_1 = '''select QuadClass,GoldsteinScale from gdelt-bq.gdeltv2.eventmentions em inner join gdelt-bq.gdeltv2.events e 
            on em.GLOBALEVENTID = e.GLOBALEVENTID
            where MonthYear >= 201901 and MonthYear <= 202001
            and (Actor1Geo_CountryCode='HK' or Actor1CountryCode='HKG');'''   


# function that connects to BigQuery client
def querys():
    client = bigquery.Client()

    # query 2 _ 1 /////////////// about 13 min 
    # query_job = client.query(query2_1)
    # results = query_job.result()  # Waits for job to complete.

    # for row in results:
    #     print(row)
    
    # # query 2 _ 2 ///////////////
    # query_job = client.query(query2_2)
    # results = query_job.result()  # Waits for job to complete.

    # for row in results:
    #     print(row)

    # query 6 ///////////////
    query_job = client.query(query6_1)
    results = query_job.result()  # Waits for job to complete.

    for row in results:
        print(row)

    # query 10 ///////////////
    query_job = client.query(query10_1)
    results = query_job.result()  # Waits for job to complete.

    for row in results:
        print(row)


if __name__ == "__main__":
    querys()