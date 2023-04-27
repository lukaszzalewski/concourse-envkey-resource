import subprocess
import sys
import json
import os

DEBUG = True if os.getenv('DEBUG') == 'true' else False
ENVKEY_SOURCE = ['test/envkey-source'] if DEBUG else ['/opt/resource/envkey-source']
ENVKEY = ['test/envkey'] if DEBUG else ['/opt/resource/envkey']

def remove_items_from_dict(original_dict,to_remove):
    vars_with_ignorded_vars = {}
    for key, value in original_dict.items():
        if key not in to_remove:
            vars_with_ignorded_vars[key] = value
    return vars_with_ignorded_vars

def run_envkey_command(args, cli_key) -> json:
    try:
        print('arguments: ', ENVKEY + ['--cli-envkey', cli_key] + args)
        res = subprocess.check_output(ENVKEY + ['--cli-envkey', cli_key] + args).decode(encoding="utf-8").rstrip()
    except subprocess.CalledProcessError as err:
        raise ValueError("ENVKEY issue")
    
    res = json.loads(res)

    if res["ok"] != True:
        raise ValueError("ENVKEY couldn't commit vars")

    return res

def run_envkey_source_command(args, env) -> json:
    try:
        print(ENVKEY_SOURCE + args)
        res = subprocess.check_output(ENVKEY_SOURCE + args, env=env).decode(encoding="utf-8").rstrip()
    except subprocess.CalledProcessError as err:
        raise ValueError("ENVKEY issue")

    if res.startswith("error: "):
        raise ValueError("ENVKEY invalid. Couldn't load vars.")

    print("res:", res)

    return json.loads(res)