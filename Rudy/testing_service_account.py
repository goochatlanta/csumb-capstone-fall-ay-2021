from google.cloud import bigquery
import datetime

# Construct a BigQuery client object.
client = bigquery.Client()

query = """
    SELECT name, SUM(number) as total_people
    FROM `bigquery-public-data.usa_names.usa_1910_2013`
    WHERE state = 'TX'
    GROUP BY name, state
    ORDER BY total_people DESC
    LIMIT 20
"""
job_config = bigquery.QueryJobConfig(use_query_cache=False)

query_job = client.query(query, job_config=job_config)  # Make an API request.

print("running  = {}".format(query_job.running()))
print("cache  = {}".format(query_job.cache_hit))
print("bytes query expected to process  = {} bytes".format(query_job.estimated_bytes_processed))
print("bytes query actually process  = {} bytes".format(query_job.total_bytes_processed))


for time in query_job.timeline:
    print("Elipse time   = {} ms".format(time._properties['elapsedMs']))


print("The query data:")
for i,row in enumerate(query_job):
    # Row values can be accessed by field name or index.
    print("name {} = {}, count = {}".format(i+1 ,row[0], row["total_people"]))

# List the 10 most recent jobs in reverse chronological order.
# Omit the max_results parameter to list jobs from the past 6 months.
print("Query History")
for job in client.list_jobs():  # API request(s)
    print("Job ID: {} : {}".format(job.job_id, job.query))

# # The following are examples of additional optional parameters:

# # Use min_creation_time and/or max_creation_time to specify a time window.
# print("Jobs from the last ten minutes:")
# ten_mins_ago = datetime.datetime.utcnow() - datetime.timedelta(minutes=10)
# for job in client.list_jobs(min_creation_time=ten_mins_ago):
#     print("{}".format(job.job_id))

# # Use all_users to include jobs run by all users in the project.
# print("Last 10 jobs run by all users:")
# for job in client.list_jobs(max_results=10, all_users=True):
#     print("{} run by user: {}".format(job.job_id, job.user_email))

# # Use state_filter to filter by job state.
# print("Last 10 jobs done:")
# for job in client.list_jobs(max_results=10, state_filter="DONE"):
#     print("{}".format(job.job_id))