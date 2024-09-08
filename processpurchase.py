import json
import boto3
import urllib
import datetime

print("Loading Function...")

def process_purchase(message, context):
     #Logging input message
     print("Received message from StepFunction")
     print(message)
     
     #Construct Response message
     response = {}
     response["TransactionType"] = message["TransactionType"]
     response["TimeStamp"] = datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")
     response["Message"] = "Hi there from process lambda function"
     
     return response
