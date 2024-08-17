import requests
import json
import os
import time
from ipfs_cid import cid_sha256_hash

bucketuuid = os.getenv("BUCKETUUID")
authentication = os.getenv("AUTHENTICATION")

# The URL of the REST API endpoint
url_upload = f'https://api.apillon.io/storage/buckets/{bucketuuid}/upload'


def post_ipfs():
    name = "double_pendulum_animation.mp4"

    # The path to the video file you want to upload
    file_path = f'./{name}'

    # Open the file in binary mode and prepare it for upload
    with open(file_path, 'rb') as file:
        headers_upload = {
            "Authorization": authentication,
            "Content-Type": "application/json"
        }

        # Define the JSON data payload
        data = {
            "files": [
                {
                    "fileName": name,
                    "contentType": "video/mp4"
                }
            ]
        }

        # Convert the data payload to a JSON string
        json_data = json.dumps(data)

        # Send the POST request with the file
        response = requests.post(url_upload, headers=headers_upload, data=json_data)
    print("ahoj")
    print(response.text)
    if not response.ok:
        print("baf")
        print(response.text)
    # to dict
    data_dict = json.loads(response.text)

    # Define the endpoint URL
    url_up = data_dict["data"]["files"][0]["url"]

    headers_up = {
        "Content-Type": "video/mp4"
    }

    # Open the file in binary mode and send the PUT request
    with open(file_path, 'rb') as file:
        response = requests.put(url_up, headers=headers_up, data=file)

        print(response)

    url_end = f'https://api.apillon.io/storage/buckets/{bucketuuid}/upload/{data_dict["data"]["sessionUuid"]}/end'

    # If there's any data to be sent with the request, define it here (for example, {})
    # In this case, no data is specified, so we send an empty JSON object.
    data = {}

    # Send the POST request
    response2 = requests.post(url_end, headers=headers_upload, json=data)

    print(response2)

    # Define the endpoint URL with bucket UUID and file UUID
    url_file = f'https://api.apillon.io/storage/buckets/{bucketuuid}/files/{data_dict["data"]["files"][0]["fileUuid"]}'

    # Headers for the GET request
    headers = {
        "Authorization": authentication  # Replace :credentials with actual base64-encoded credentials
    }
    cid = None
    n = 0
    while cid is None and n <= 10:
        # Send the GET request
        time.sleep(5)
        response = requests.get(url_file, headers=headers)
        data_dict2 = json.loads(response.text)
        cid = data_dict2["data"]["CID"]
        n += 1
    print(f"first: {cid}")
    return cid


def post_json_ipfs(cid, n_pendulums, d_diff, t_max, g, m1, m2, L1, L2, theta1, theta2):
    print(cid)
    # create json metadata
    # get initial conditions to metadata
    metadata = """
        {{
          "name": "Double Pendulum",
          "description": "Hi, my name is Klára and I'm currently studying mathematical modeling at university. 
          
          This collection of NFTs is connecting world of modeling physics and crypto. 
          As you can see, even the slightest change in initial conditions is resulting to completely 
          different trajectories of pendulums. This effect is called deterministic chaos. 
          It means that despite the fact that we have complete equations describing its motion, 
          we can never predict said motion for long time, it appears chaotic, 
          because we can't measure initial conditions exactly. 
          
          I used this principle to generate completely unique NFTs so You can (and already did) generate 
          Yours original NFT.
          
          Technical info: I used Classic Runge-Kutta method for numerical solving 
          Hamilton's canonical equations of double pendulum motion.
          
          I hope You are enjoying cute animation <3.",
          "image": "ipfs://{0}",
          "attributes": [
            {{
              "trait_type": "Number of Pendulums",
              "value": "{1}"
            }},
            {{
              "trait_type": "Difference of pendulums",
              "value": "{2}"
            }},
            {{
              "trait_type": "Simulation length",
              "value": "{3}"
            }},
            {{
              "trait_type": "Gravitational acceleration",
              "value": "{4}"
            }},
            {{
              "trait_type": "Mass 1",
              "value": "{5}"
            }},
            {{
              "trait_type": "Mass 2",
              "value": "{6}"
            }},
            {{
              "trait_type": "Length 1",
              "value": "{7}"
            }},
            {{
              "trait_type": "Length 2",
              "value": "{8}"
            }},
            {{
              "trait_type": "Theta 1",
              "value": "{9}"
            }},
            {{
              "trait_type": "Theta 2",
              "value": "{10}"
            }}
          ]
        }}
        """.format(cid, n_pendulums, d_diff, t_max, g, m1, m2, L1, L2, theta1, theta2)

    metadata_json = json.dumps(metadata)

    headers_upload2 = {
        "Authorization": authentication,
        "Content-Type": "application/json"
    }

    data = {
        "files": [
            {
                "fileName": "metadata.json",
                "contentType": "application/json"
            }
        ]
    }

    json_data = json.dumps(data)

    # Send the POST request with the file
    response = requests.post(url_upload, headers=headers_upload2, data=json_data)

    data_dict2 = json.loads(response.text)

    # Define the endpoint URL
    url_up = data_dict2["data"]["files"][0]["url"]

    headers_up = {
        "Content-Type": "application/json"
    }

    # Open the file in binary mode and send the PUT request
    response = requests.put(url_up, headers=headers_up, data=metadata_json)

    url_end = f'https://api.apillon.io/storage/buckets/{bucketuuid}/upload/{data_dict2["data"]["sessionUuid"]}/end'

    # If there's any data to be sent with the request, define it here (for example, {})
    # In this case, no data is specified, so we send an empty JSON object.
    data = {}

    # Send the POST request
    response2 = requests.post(url_end, headers=headers_upload2, json=data)

    # Define the endpoint URL with bucket UUID and file UUID
    url_file = f'https://api.apillon.io/storage/buckets/{bucketuuid}/files/{data_dict2["data"]["files"][0]["fileUuid"]}'

    # Headers for the GET request
    headers = {
        "Authorization": authentication
    }

    cid2 = None
    n = 0
    while cid2 is None and n <= 10:
        # Send the GET request
        time.sleep(5)
        response = requests.get(url_file, headers=headers)
        data_dict2 = json.loads(response.text)
        cid2 = data_dict2["data"]["CID"]
        n += 1
    return cid2


def get_initial_conditions(n_pendulums, d_diff, t_max, g, m1, m2, L1, L2, theta1, theta2, colormap, background):
    return n_pendulums, d_diff, t_max, g, m1, m2, L1, L2, theta1, theta2, colormap, background


def get_cid():
    name = "double_pendulum_animation.mp4"

    # The path to the video file you want to upload
    file_path = f'./{name}'

    # calculate cid
    cid = cid_sha256_hash(open(file_path, 'rb').read())
    print(cid)

    metadata = """
            {{
              "name": "Double Pendulum",
              "description": "",
              "image": "ipfs://{0}",
              "attributes": [
                {{
                  "trait_type": "Color",
                  "value": "Blue"
                }},
                {{
                  "trait_type": "Size",
                  "value": "Large"
                }}
              ]
            }}
            """.format(cid)

    metadata_json = json.dumps(metadata)

    # calculate cid
    cid2 = cid_sha256_hash(metadata_json.encode('utf-8'))
    print(cid2)
    return cid2, metadata_json
