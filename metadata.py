import requests
import json

def get_instance_metadata():
    base_url = "http://169.254.169.254/latest/meta-data/"
    metadata_keys = [
        "ami-id", "instance-id", "instance-type", "hostname", "local-ipv4", "availability-zones", "security-groups", "subnet-id", "vpc-id"
    ]
    metadata = {}

    for key in metadata_keys:
        try:
            response = requests.get(base_url + key, timeout=2)
            if response.status_code == 200:
                metadata[key] = response.text
            else:
                metadata[key] = "N/A"
        except requests.exceptions.RequestException:
            metadata[key] = "Error retrieving the data"

    retun metadata
    
if __name__ == "__main__":
    metadata = get_instance_metadata()
    print(json.dumps(metadata, indent=4))
