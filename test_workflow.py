# Databricks notebook source
import json
databricks_runid=json.loads(dbutils.notebook.entry_point.getDbutils().notebook().getContext().toJson())['tags']['multitaskParentRunId']

# COMMAND ----------

print("commit new changes")

# COMMAND ----------

print("without pull")
