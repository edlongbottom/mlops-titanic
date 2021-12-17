# End-to-end Machine Learning workflow

This project attempts to demonstrate a typical end-to-end machine learning workflow in Python, from data exploration to model training and deployment. It is broken up into two phases: Experimentation (which includes exploratory data analysis, feature engineering, model training and evaluation) and Deployment (which includes web service development, containerisation using Docker and deployment to Kubernetes).

The deployment scripts have been designed to be transferrable for use in other projects or ML models without the need for any additional code (only changes to a config file required). This is intended as a set of scripts for automating the deployment of ML models to Kubernetes as prediction web services.  

The Titanic classification dataset from Kaggle is used as a simple use case to demonstrate the workflow. 


### Experimentation

This folder contains the datasets, model repository and jupyter notebooks used during the project experimentation phase. 
 - datasets: train and test data from Kaggle in CSV files
 - models: a folder for storing ML model *.pkl files
 - notebooks: Jupyter notebooks documenting approaches for EDA and model development, training and evaluation

A requirements.txt file in this folder lists the python packages required to run the notebooks.


### Deployment

This folder contains the scripts required to deploy a machine learning model as a RESTful prediction web service to a kubernetes instance. Flask is used to create a simple REST API wrapper for the latest ML model produced during Experimentation. A Dockerfile and Helm chart are then used for the automated deployment and exposure of the model as a prediction web service on Kubernetes. 

The deployment-k8s.ipynb Jupyter notebook outlines the steps for the deployment.

A requirements.txt file in this folder lists the python packages required to run the prediction web service.