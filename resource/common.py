import subprocess
import sys
import json

def remove_items_from_dict(original_dict,to_remove):
    vars_with_ignorded_vars = {}
    for key, value in original_dict.items():
        if key not in to_remove:
            vars_with_ignorded_vars[key] = value

def run_envkey_command(args, env):
  try:
    res = subprocess.check_output(args, env=env).decode(encoding="utf-8").rstrip()
  except subprocess.CalledProcessError as err:
    print("envkey-source " + err.output.decode(encoding="utf-8"), file=sys.stderr)
    raise ValueError("ENVKEY issue")

  if res.startswith("error: "):
    raise ValueError("ENVKEY invalid. Couldn't load vars.")

  return json.loads(res)