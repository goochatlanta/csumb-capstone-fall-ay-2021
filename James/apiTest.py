from google.cloud import bigquery
import os
import pprint
from google.cloud.bigquery.client import Client
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'C:\\Users\\james\\Downloads\\james-nps-drmi-33ea3436d5d7.json'

# Construct a BigQuery client object.
client = bigquery.Client()

job_config = bigquery.QueryJobConfig(use_query_cache=False)
query = """
    SELECT name, SUM(number) as total_people
    FROM `bigquery-public-data.usa_names.usa_1910_2013`
    WHERE state = 'TX'
    GROUP BY name, state
    ORDER BY total_people DESC
    LIMIT 20
"""



query_job = client.query(query, job_config=job_config)  # Make an API request.







print("The query data:")

for row in query_job:
    # Row values can be accessed by field name or index.
    print("name={}, count={}".format(row[0], row["total_people"]))
	
	

print('Estimated bytes to process: {}'.format(query_job.estimated_bytes_processed))
print('Total bytes processed: {}'.format(query_job.total_bytes_processed))
#the below statements return the dictionary list of my query_job. 
#Here you can find the execution of the query in the timeline attribute
pprint.pprint(query_job.__dict__)

