## End to End data science project

import dagshub
dagshub.init(repo_owner='NidhiMehta1444', repo_name='ML-project', mlflow=True)

import mlflow
with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)