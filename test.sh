#!/bin/bash

command="aws compute-optimizer export-ec2-instance-recommendations --s3-destination-config bucket=testbucket,keyPrefix=test/"

# Execute the AWS CLI command
output=$(eval $command 2>&1)

if [ $? -eq 0 ]; then
  echo "Command executed successfully"
  
  # Upload a success message to an S3 bucket using the AWS CLI
  echo "Command executed successfully" | aws s3 cp - s3://testbucket/test/success.txt
else
  echo "Command execution failed: $output"
fi
