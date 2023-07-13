import subprocess
import os

def lambda_handler(event, context):
    try:
        aws_cli_path = "/opt/awscli/aws"
        command = f"{aws_cli_path} compute-optimizer export-ec2-instance-recommendations --s3-destination-config bucket=testbucket"
        
        output = subprocess.check_output(command.split(), stderr=subprocess.STDOUT)
        output = output.decode('utf-8').strip()

        return {
            'statusCode': 200,
            'body': f'Command output: {output}'
        }
    except subprocess.CalledProcessError as e:
        return {
            'statusCode': 500,
            'body': f'Error executing AWS CLI command: {str(e.output)}'
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': f'Error: {str(e)}'
        }
