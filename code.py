import subprocess
import boto3

def lambda_handler(event, context):
    command = "aws compute-optimizer export-ec2-instance-recommendations --s3-destination-config bucket=testbucket,keyPrefix=test/"
    
    try:
        subprocess.check_output(command, shell=True)
        
        # Upload a success message to an S3 bucket using boto3
        s3 = boto3.client('s3')
        s3.put_object(Body='Command executed successfully', Bucket='testbucket', Key='test/success.txt')
        
        return {
            'statusCode': 200,
            'body': 'Command executed successfully'
        }
    except subprocess.CalledProcessError as e:
        return {
            'statusCode': 500,
            'body': f'Command execution failed: {e.output.decode()}'
        }
