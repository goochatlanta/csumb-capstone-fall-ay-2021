import mysql.connector
from mysql.connector import Error
from decouple import config
import csv
# from time import time
import datetime

# grabing env variables
host = config('HOST')
database = config('DATABASE')
user = config('gdeltUSER')
password = config('PASSWORD')


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

# 6.Top 30 most important articles that happened in the US about 
# specific areas, for example China? What is the average tone 
# and importance in the impact of these articles? 
# /////////////////////////////////////////////////////////////
# RUN : 30 rows in set (3 min 5.69 sec) 
query6_1 = ''' select GoldsteinScale, Avgtone, NumMentions from events 
               where (Actor1Geo_CountryCode='CH' or Actor2Geo_CountryCode='CH')
               and ActionGeo_CountryCode='US'  
               order by NumMentions desc limit 30;'''


# 10.Get the quadclass and GoldsteinScale of events occuring in China specifically Hong Kong. 
# *Note: Will expand upon this further
# /////////////////////////////////////////////////////////////
# RUN : 53141 rows in set (3 min 45.74 sec)
query10_1 = '''select QuadClass,GoldsteinScale from eventmentions em inner join events e 
            on em.GLOBALEVENTID = e.GLOBALEVENTID
            where MonthYear >= 201901 and MonthYear <= 202001
            and (Actor1Geo_CountryCode='HK' or Actor1CountryCode='HKG');'''   

queryt = []
time  = []
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
        
                
        # Query 6  ////////////////
        init_time = datetime.datetime.now()
        cursor.execute(query6_1)
        end_time = datetime.datetime.now()
        exec_time =  end_time - init_time
        print ( 'exec_time  = {} seconds '.format( exec_time.seconds)  )
        queryt.append('query 6')
        time.append(exec_time.seconds)
        # iterate over result and write to csv file
        with open('query6_1.csv', 'w') as csvfile:
            # creating a csv writer object 
            csvwriter = csv.writer(csvfile) 
            csvwriter.writerow([ 'GoldsteinScale', 'Avgtone', 'NumMentions' ])
            # writing the fields 
            for row in cursor:
                csvwriter.writerow([row[0], row[1], row[2]])
        #///////////////////////////////
        
        # Query 10 ////////////////
        init_time = datetime.datetime.now()
        cursor.execute(query10_1)
        end_time = datetime.datetime.now()
        exec_time =  end_time - init_time
        print ( 'exec_time  = {} seconds '.format( exec_time.seconds)  )
        queryt.append('query 10')
        time.append(exec_time.seconds)
        # iterate over result and write to csv file
        with open('query10_1.csv', 'w') as csvfile:
            # creating a csv writer object
            csvwriter = csv.writer(csvfile) 

            # writing the fields
            csvwriter.writerow([ 'QuadClass', 'GoldsteinScale'])
            for row in cursor:
                csvwriter.writerow([row[0], row[1]])
        #///////////////////////////////

        # Query 2_1 ////////////////
        init_time = datetime.datetime.now()
        cursor.execute(query2_1)
        end_time = datetime.datetime.now()
        exec_time =  end_time - init_time
        print ( 'exec_time  = {} seconds '.format( exec_time.seconds)  )
        queryt.append('query 2_1')
        time.append(exec_time.seconds)
        # iterate over result and write to csv file
        with open('query2_1.csv', 'w') as csvfile:
            # creating a csv writer object
            csvwriter = csv.writer(csvfile) 

            # writing the fields
            csvwriter.writerow([ 'Count'])
            for row in cursor:
                csvwriter.writerow(row)
        #///////////////////////////////

        # Query 2_1 ////////////////
        init_time = datetime.datetime.now()
        cursor.execute(query2_2)
        end_time = datetime.datetime.now()
        exec_time =  end_time - init_time
        print ( 'exec_time  = {} seconds '.format( exec_time.seconds)  )
        queryt.append('query 2_2')
        time.append(exec_time.seconds)
        # iterate over result and write to csv file
        with open('query2_2.csv', 'w') as csvfile:
            # creating a csv writer object
            csvwriter = csv.writer(csvfile) 

            # writing the fields
            csvwriter.writerow([ 'Count'])
            for row in cursor:
                csvwriter.writerow(row)
        #///////////////////////////////


except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")


with open('query_time.csv', 'w') as csvfile:
            # creating a csv writer object
            csvwriter = csv.writer(csvfile) 

            # writing the fields
            csvwriter.writerow([ 'Query', 'Time(sec)'])
            for i,x in enumerate(time):
                csvwriter.writerow([queryt[i], time[i]])
    