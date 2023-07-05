# Databricks notebook source
import sys
import os
sys.path.append(os.path.abspath('..'))

# COMMAND ----------

import sys
sys.path.append("/Workspace/Repos/avinash.shukla@capgemini.com/files_in_repos")

# COMMAND ----------

from utils.sample2 import cube_root
cube_root(8)

# COMMAND ----------

/Workspace/Repos/avinash.shukla@capgemini.com/files_in_repos/utils/sample2.py

# COMMAND ----------

import sys
import os
sys.path.append(os.path.abspath('..'))

# COMMAND ----------

import sys
sys.path.append("Workspace/Repos/avinash.shukla@capgemini.com/sage")

# COMMAND ----------

from external_system.s3_to_snowflake import S3ToSnowflake

# COMMAND ----------

sys.path.append(os.path.abspath('/Workspace/Repos/<username>/supplemental_files'))

# COMMAND ----------

# MAGIC %sh ssh -i /dbfs:/FileStore/tables/idea_demo_main_key.pem -L 27017:34.236.42.155:27021 ec2-user@idea-demo-main-docdb.cluster-ciiky6du2jjt.us-east-1.docdb.amazonaws.com

# COMMAND ----------


