import boto3
from datetime import datetime

def generate_backup():
    date_format      = "%d/%m/%Y"
    date_time_format = "%d-%m-%Y_%H_%M_%S"
    created_by_value = "lambda_ec2_backup-script"
    inst_name_prefix = "lambda_ec2_backup"
    backup_tag       = "backup"
    inst_name        = ""
    
    start_time = datetime.now()
    
    ec2_client = boto3.client('ec2')
    regions = ec2_client.describe_regions()
    ec2_client = boto3.client('ec2', region_name='us-east-1')
    
    instances = ec2_client.describe_instances()
    for reservation in instances['Reservations']:
        for instance in reservation['Instances']:
            
            for tag in instance['Tags']:
                if tag['Key'] == 'Name':
                    inst_name = tag['Value']
                if tag['Key'] == 'backup':
                    print(tag['Value'])
                    if tag['Value'] == 'true':
                        if instance['State']['Name'] == "running" \
                            or instance['State']['Name'] == "stopping" \
                            or instance['State']['Name'] == "stopped":
                            date_time = datetime.now().strftime(date_time_format)
                            date = datetime.now().strftime(date_format)
                            
                            ami_name = inst_name_prefix + "_" + inst_name + "_" +  date_time
                            ami_desc = ami_name
                            
                            print "Storing: " + inst_name + " as " + ami_desc
                            
                            # AMI Creation
                            ami_id = ec2_client.create_image(InstanceId=instance['InstanceId'], \
                            Name=ami_name, Description=ami_desc, \
                            NoReboot=True)
                            # AMI Tagging                                
                            ec2_client.create_tags(Resources=[ami_id['ImageId']], \
                            Tags=[{'Key': 'creation_date','Value': date}, \
                            {'Key': 'created_by', 'Value': created_by_value}])
                else:
                    print("No backup tags. Ignoring backup of instance: " + inst_name)
                            
    end_time = datetime.now()
    took_time = end_time - start_time
    print "Total execution time: " + str(took_time)
    
def lambda_handler(event, context):
    generate_backup()
