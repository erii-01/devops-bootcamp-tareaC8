import boto3

def securitygroups():
    ec2 = boto3.resource('ec2')
    try:    
        response = list(ec2.security_groups.all())
        print("Se encontraron los siguientes security groups:")
        for sg in response:
            print(sg.id)
    except Exception as err:
        print(err)

if __name__ == "__main__": 
    securitygroups()
