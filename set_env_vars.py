import requests
import argparse
import json


def update_env_vars(token, env, env_var_key_value):
    # url = f"{HOSTNAME}/api/v3/repos/{OWNER}/{REPO}/environments/{ENVIRONMENT_NAME}/variables"
    url = f"https://api.github.com/repos/VaderKB/devops-project-2/environments/{env}/variables"

    get_patch_url = url + f"/{env_var_key_value['name']}"


    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {token}",
        "X-GitHub-Api-Version": "2022-11-28"
    }

    # env_var_key_value = {
    #     "name": "USERNAME",
    #     "value": "octocat1"
    # }

    response = requests.get(get_patch_url, headers=headers)
    print("Get status code:", response.status_code)

    if response.status_code == 200:
        print(f"ENV variable {env_var_key_value['name']} already exists")
        response_json = response.json()
        if response_json['value'] == env_var_key_value['value']:
            print(f"ENV variable {env_var_key_value['name']} existing value: {response_json['value']} is same as value to be updated: {env_var_key_value['value']}")
        else:
            response = requests.patch(get_patch_url, headers=headers, json=env_var_key_value)
            print(f"ENV variable {env_var_key_value['name']} value updated to: {env_var_key_value['value']} from: {response_json['value']}")
    else:
        print(f"Creating ENV variable {env_var_key_value['name']} with value: {env_var_key_value['value']}")
        response = requests.post(url, headers=headers, json=env_var_key_value)
    
def get_env_configurations(env):
    
    env_character = env[0]
    with open(f'{env_character}.json') as json_file:
        env_config = json.load(json_file)
    return env_config

    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process some arguments.")
    parser.add_argument("token", type=str, help="First argument")
    parser.add_argument("env", type=str, help="Second argument")

    args = parser.parse_args()

    print(f"Argument 1: {args.token}")
    print(f"Argument 2: {args.env}")
    
    env_config = get_env_configurations(args.env)
    print(env_config)

    for outer_key in env_config.keys():
        for nested_key in env_config[outer_key]:

            env_var_key_value = {"name": nested_key,
                                 "value": env_config[outer_key][nested_key]}

            update_env_vars(args.token, args.env, env_var_key_value)

            env_var_key_value_tf = {"name": "TF_VAR_"+nested_key,
                                 "value": env_config[outer_key][nested_key]}
            
            update_env_vars(args.token, args.env, env_var_key_value_tf)

    # update_env_vars(args.token, args.env)

