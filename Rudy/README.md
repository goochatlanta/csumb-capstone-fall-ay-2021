September 9, 2020 - Notes

**BigQuery understanding Partition Tables**

- Partition Tables - tables that are divided into segments called partitions , that make it easier to manage and query data. By dividing tables into smaller partition this can improve query performance. 

- Ingestions Time - tables that are partitioned based on the data's ingestion time or arrivel time.

- When you create table partitioned by ingestion time, BigQuery automatically loads data into daily.

- Ingestion-time partitioned tables includes a pseudo column _PARTITIONTIME that contains a data-based timestamp for data that is loaded into the table. 

- Queries agains partitoned table can restrict the data read by supplying _PARTITIONTIME filters that represent a partition's loaction

- All the data in the specified partiton is read by the query, but the _PARTITIONTIME predicate filter restricts the number of partitions scanned.

- Get info about partitioned tables using a table called meta tables. 

**Events Tables**

- Actor(1/2)code - code for Actor(includes geographic, class, ethnic, religion, and type class).

- ActorType1code - 3-character CAMOE code type or role of actor. This can be specified role such as piloce force, etc...

- AveTone - average tone of all documents containing one or more mentions of this event during the 15 min update. 

**Questions**

    - Top 30 most important US press articles about specific areas, for example China? What is the average tone and importance in the impact of these articles?

    - What type of data is shown in articles of countries that are more restricted for example communist countries like China? Does it look regulated? 

    -  What type of data sources are mostly used in the US. What about China? 
**10-1-20**
- Wrote simple python script that can run queries.
- The queries that we were creating will hit data tables that as large as 280GB and 150GB. I was reading about how make my queries faster this one good artilce that I read 
https://mode.com/sql-tutorial/sql-performance-tuning/
- One of the ways to make it quicker was to use smaller tables to cut down the information that we are looking at. 
- also run a few queries to figure out how many tables each where clause was running for example this query:  "explain select AvgTone from events where (Actor1Geo_CountryCode= 'US' or Actor2Geo_CountryCode= 'US');"
this query return 426817362 rows