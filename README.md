# AWS-instance-metadata
This project is to get instance metadata
### Pre-requisites ###
- Python should be installed in ec2 where you are executing the code.
  `sudo yum install epel-release`
  `sudo yum install python3`

- Now install requests using pip
 `pip3 install requests`

### How to Run the code ###
- Log into the EC2 server and then make sure all the pre-requisites are installed (by default in some OS it is installed)
- Copy or create a metadata.py script and try to run it using `python metadata.py`
- If you are trying to run the script out of EC2 it won't work.

### What's in the Output ###
- As mentioned in the script it can fetch "ami-id", "instance-id", "instance-type", "hostname", "local-ipv4", "availability-zones", "security-groups", "subnet-id", "vpc-id" these details into JSON file.
