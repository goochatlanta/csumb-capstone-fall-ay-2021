# CSUMB Capstone Fall AY 2021
Further development of the backend for the GDELT Browser-based Access Tool (GBBAT). The backend will be connected to Google's BigQuery. 

## Semester Goal: Overview
1. Re-wire GBBAT prototype from AWS to BigQuery
2. Analyze quality of `eventmentions` observations that are linked to `events` with Chinese actor. Looking for *trash* articles. 
3. Give GBBAT access to at least one *theme* column of the `GKG` table. 

## AWS
create .env file in backend folder and paste these parameters in that file

>HOST=gdelt-events-mentions.cbghl9qobm13.us-east-2.rds.amazonaws.com

>gdeltUSER=admin

>PASSWORD=R1m23&!#Bto

>DATABASE=gdelt

## Trainings

[How to guides](https://cloud.google.com/bigquery/docs)

- [Data Engineering, Big Data, and Machine Learning on GCP Specialization](https://www.coursera.org/specializations/gcp-data-machine-learning?edocomorp=GCPtraining0419)
- The [Modernizing Data Lakes and Data Warehouses with GCP](https://www.coursera.org/learn/data-lakes-data-warehouses-gcp?specialization=gcp-data-machine-learning#syllabus) is a prime area to start in. Pay specific attention to lessons on clustering, partitioning, cost control, and query performance. I would skip around to the courses of interest, specifically focusing on any pieces of the courses on Data Warehousing or BigQuery.
- [BigQuery in a Minute (Youtube)](https://www.youtube.com/watch?v=CFw4peH2UwU)
- [Partitioning and Clustering with BigQuery - Take5 YouTube Series](https://www.youtube.com/watch?v=qqbYrQGSibQ)
- [Controlling costs in BigQuery](https://cloud.google.com/bigquery/docs/best-practices-costs)
- A [partitioned table](https://cloud.google.com/bigquery/docs/partitioned-tables) is a special table that is divided into segments, called partitions, that make it easier to manage and query your data. By dividing a large table into smaller partitions, you can improve query performance, and you can control costs by reducing the number of bytes read by a query. 
- [Clustered tables](https://cloud.google.com/bigquery/docs/clustered-tables)
- [Best practices for query performance](https://cloud.google.com/bigquery/docs/best-practices-performance-overview)