import mysql.connector
from mysql.connector import Error
from decouple import config

# grabing env variables
host = config('HOST')
database = config('DATABASE')
user = config('gdeltUSER')
password = config('PASSWORD')

# query test
query_test = '''select AvgTone 
                   from events limit 10;'''
# 1. What is the average tone of articles written about 
# the US by the Chinese press in March 2018? What about March 2019?
# /////////////////////////////////////////////////////////////
# March 2019 
# RUN : 11453 rows in set (14 min 43.04 sec)
query1_2 = '''select avg(AvgTone) from events e 
            inner join eventmentions m on e.GLOBALEVENTID=m.GLOBALEVENTID  
            WHERE (MentionSourceName LIKE '%xinhuanet.com%' 
            OR MentionSourceName LIKE '%chinadaily.com.cn%' 
            OR MentionSourceName LIKE '%china.org.cn%' 
            OR MentionSourceName LIKE '%ecns.cn%' 
            OR MentionSourceName LIKE '%peopledaily.com.cn%') 
            and (Actor1Geo_CountryCode= 'US' or Actor2Geo_CountryCode= 'US') 
            and MonthYear=201803;'''

# March 2018
query1_2 = '''select avg(AvgTone) from events e 
              inner join eventmentions m on e.GLOBALEVENTID=m.GLOBALEVENTID  
              WHERE (MentionSourceName LIKE '%xinhuanet.com%' 
              OR MentionSourceName LIKE '%chinadaily.com.cn%' 
              OR MentionSourceName LIKE '%china.org.cn%' 
              OR MentionSourceName LIKE '%ecns.cn%' 
              OR MentionSourceName LIKE '%peopledaily.com.cn%') 
              and (Actor1Geo_CountryCode= 'US' or Actor2Geo_CountryCode= 'US') 
              and MonthYear=201803;'''


# 2. How many articles did the New York Times write about 
# China in July 2016? What about July 2017? 
# /////////////////////////////////////////////////////////////
# July 2016
# RUN : 1 row in set (7 min 53.19 sec)
query2_1 = '''select count(*) from eventmentions m 
              inner join events e on e.GLOBALEVENTID=m.GLOBALEVENTID 
              where m.MentionSourceName LIKE '%nytimes.com%' 
              and e.MonthYear=201607 
              and (Actor1Geo_CountryCode= 'US' or Actor2Geo_CountryCode= 'US') 
              and ActionGeo_CountryCode='US';'''
# July 2017
query2_2 = '''select count(*) from eventmentions m 
              inner join events e on e.GLOBALEVENTID=m.GLOBALEVENTID 
              where m.MentionSourceName LIKE '%nytimes.com%' 
              and e.MonthYear=201707 
              and (Actor1Geo_CountryCode= 'US' or Actor2Geo_CountryCode= 'US') 
              and ActionGeo_CountryCode='US';'''

# 3.What are the top 20 sources of articles written 
# about Thailand in January through March 2019? 
# /////////////////////////////////////////////////////////////
# RUN : 6769 rows in set (8 min 1.12 sec)
query3_1 = '''select MentionSourceName from eventmentions em 
                inner join events e on em.GLOBALEVENTID = e.GLOBALEVENTID 
                where MonthYear >= 201901 
                and MonthYear <= 201903 
                and (Actor1Geo_CountryCode='Th' or Actor1CountryCode='THA') 
                group by MentionSourceName 
                order by count(NumArticles) 
                desc'''   


# 4. In July 2018, what percentage of articles about China n the 
# eventmentions table have confidence level 0? What about confidence 
# level 30? 50? 100? Will you please do that same 
# analysis for articles about the US?
# /////////////////////////////////////////////////////////////
# RUN : did not finish more the 1 hr
condfidenceLevels = [0, 30, 50, 100]
queries4_1_china =[]
# China confidence
for i in condfidenceLevels:
    queries4_1_china.append('''select count(*) from eventmentions m 
              inner join  events e on e.GLOBALEVENTID=m.GLOBALEVENTID 
              where ActionGeo_CountryCode='CH' 
              or (Actor1Geo_CountryCode= 'CH' or Actor2Geo_CountryCode= 'CH') 
              and Confidence >= '''+ str(i) + ''';''')

# US confidence
queries4_1_us =[]
for i in condfidenceLevels:
    queries4_1_us.append('''select count(*) from eventmentions m 
              inner join  events e on e.GLOBALEVENTID=m.GLOBALEVENTID 
              where ActionGeo_CountryCode='US' 
              or (Actor1Geo_CountryCode= 'US' or Actor2Geo_CountryCode= 'US') 
              and Confidence >= '''+ str(i) + ''';''')


# 5. Can you please explore what the article length is for 
# articles in the eventmentions table in the first two weeks 
# of January 2017? What is the longest article? The shortage? 
# What percentage of articles are less than 10 words?
# RUN : 
queries5_1 = '''select MentionDocLen from eventmentions 
                where EventTimeDate >= 201701010000 
                and EventTimeDate <= 201701150000;'''



# 6.Top 30 most important articles that happened in the US about 
# specific areas, for example China? What is the average tone 
# and importance in the impact of these articles? 
# /////////////////////////////////////////////////////////////
# RUN : 30 rows in set (3 min 5.69 sec) in MySQL instance
query6_1 = ''' select GoldsteinScale, Avgtone, NumMentions from events 
               where (Actor1Geo_CountryCode='CH' or Actor2Geo_CountryCode='CH')
               and ActionGeo_CountryCode='US'  
               order by NumMentions desc limit 30;'''


# 7.What type of data is shown in articles of countries that 
# are more restricted for example communist countries like China? 
# Does it look regulated? 
# /////////////////////////////////////////////////////////////
# RUN : Lost connection to MySQL server during query
query7_1 = '''select Actor1Type1Code, count(Actor1Type1Code) as ord 
              from events e inner join eventmentions m on e.GLOBALEVENTID=m.GLOBALEVENTID  
              where ( MentionSourceName LIKE '%xinhuanet.com%' 
              OR MentionSourceName LIKE '%chinadaily.com.cn%' 
              OR MentionSourceName LIKE '%china.org.cn%' 
              OR  MentionSourceName LIKE '%ecns.cn%' 
              OR MentionSourceName LIKE '%peopledaily.com.cn%') 
              and (Actor1Geo_CountryCode='CH' or Actor2Geo_CountryCode='CH') 
              or ActionGeo_CountryCode='CH' 
              group by Actor1Type1Code 
              order by ord desc;'''


# 8.What type of data sources are mostly used in the US. What about China? 
# /////////////////////////////////////////////////////////////
# RUN :
query8_1 = '''select MentionType, count(MentionType) as c 
              from eventmentions m inner join events e on m.GLOBALEVENTID=e.GLOBALEVENTID 
              where (Actor1Geo_CountryCode='CH' or Actor2Geo_CountryCode='CH') 
              and ActionGeo_CountryCode='CH' 
              group by MentionType 
              order by c desc;'''

# 9.Count the # of CHZ publications that mention the united states and map the data by region.
# /////////////////////////////////////////////////////////////
# RUN : * 
query9_1 = '''select count(NumArticles) from eventmentions em inner join events e
            on em.GLOBALEVENTID = e.GLOBALEVENTID 
            where Actor2Geo_Fullname='United States' and (Actor1Geo_CountryCode='CH' or Actor1CountryCode='CHZ');'''


# 10.Get the quadclass and GoldsteinScale of events occuring in China specifically Hong Kong. 
# *Note: Will expand upon this further
# /////////////////////////////////////////////////////////////
# RUN : 53141 rows in set (3 min 45.74 sec)
query10_1 = '''select QuadClass,GoldsteinScale from eventmentions em inner join events e 
            on em.GLOBALEVENTID = e.GLOBALEVENTID
            where MonthYear >= 201901 and MonthYear <= 202001
            and (Actor1Geo_CountryCode='HK' or Actor1CountryCode='HKG');'''    

information  = []

# Connecting to database and running queries
try:
    connection = mysql.connector.connect(host=host,
                                         database=database,
                                         user=user,
                                         password=password)
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        
        #Query Test ////////////////
        cursor.execute(query_test)
        # iterate over result
        for row in cursor:
            print(row)

except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")