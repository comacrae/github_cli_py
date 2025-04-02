import json
from os import path
from typing import Optional, Mapping

def load_json_resource(
    dirpath:str =r"C:\Users\comac\github_cli_py\github_cli_py\tests\resources", 
    filename:Optional[str] = None) -> Mapping:
  """Makes it easy to read json responses to test event type commits"""
  if filename is None:
    raise TypeError("Filename parameter must be defined")
  full_path : str = path.join(dirpath,filename)
  with open(full_path, "r",errors="ignore") as f:
    return json.load(f)

