# Resume
Hello Mariano.
Along with saying hello, I commented that this challenge was very entertaining, so thank you very much for the opportunity.
Now I will give you a summary of how I approached the problem:

Thinking that an ETL solution is needed for the Analytics area, I used the Kedro framework which is created in Python and is perfect for developing ML projects. Here's a little description:

* [Introducing Kedro: The Open Source Library for Production-Ready Machine Learning Code](https://medium.com/quantumblack/introducing-kedro-the-open-source-library-for-production-ready-machine-learning-code-d1c6d26ce2cf)

The basic architecture of kedro consists of three types of objects:
 1) A "catalog" is a source of information that can be a GCP Bucket, CSV, Parquet, JSON, BigQuery Table and others, which    you declare in a YML file.
2) A "node" is the function where you will use the catalogs as inputs and outputs.
3) And finally a "pipeline" is the grouping of several nodes.



# Data Engineer - Challenge
This is the Basic Challenge for Data Engineers. 

Lider.cl wants to create a new shiny section for videogames, to bring custom videogame information to our clients, our Analytics team needs a new report each day with several videogames information. This information will be used to create a lot of ML models & Data Science to give our customers the best experience and make the best decision of which videogame buy.

For this Challenge, we want you to do a Job who give us the Data for the Analytics team, but with a few concerns:
- The Job must be an ETL code in Java or Scala or Python.
- We need the Data Model for the problem.
- And we want a Deployment for this code.

## ETL Job
The job must receive the datasets & brings a few things:
- The top 10 best games for each console/company.
- The worst 10 games for each console/company.
- The top 10 best games for all consoles.
- The worst 10 games for all consoles.
The data is in the folder data/ in the root. The report can be exposed in any way you want, but remember this is an ETL Job.

## Data Model
The Data Model must be in 3NF. 
Save the model in the DataModel folder in both formats (data model format & JPG/PNG).
```
Use any tool, but please tell us the tool you choose & why.
```

## Deployment 
We want you to give us the way to deploy your job and run it in any environment, So please put the way to deploy very clearly.

## Concerns
- You can create a new README for anything you want to tell us. Please don't name README.md
- We want to see if you know how to code in a professional way, so use the best practices of Software Engineering!.
- This is an ETL Job, so show us all you know about good practices to do ETL's.
- Save all the changes in your personal GitHub account using a Fork from this repository and send us the link to clone and see the repository.


### Disclaimer Note
"This challenge is your cover letter, the elections you choose to do & not to do matters, and will be ask in the next interview"


## Datasets
We use the data from TopGames provided by Metascore.

* [Kaggle: Metacritic reviewed games since 2000](https://www.kaggle.com/destring/metacritic-reviewed-games-since-2000)


