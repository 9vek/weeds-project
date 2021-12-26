import json
from pathlib import Path

def generate_config(store_path, path_type):
  store_path = Path(store_path).joinpath('weeds\\')
  store_path = store_path.absolute() if path_type == 'a' else store_path.relative_to('./')
  config = {
      'store_path': store_path.as_posix(), 
      'path_type': path_type,
      'size_limit_mb': 1000,
      'weeds': [
        
      ],
      'ignore_files': [
        'desktop.ini',
      ],
      'doc_folder': [
        '.*pdf$', '.*doc$', '.*docx$', '.*ppt$', '.*pptx$', '.*md$'
      ],
      'exe_folder': [
        '.*exe$', '.*msi$'
      ],
      'img_folder': [
        '.*jpg$', '.*png$', '.*gif$'
      ],
      'zip_folder': [
        '.*rar$', '.*zip$', '.*7z$'
      ]
    }
  return config


def has_config():
    if Path('weeds.json').exists():
        return True
    else:
        return False


def save_config(config):
  file_path = Path('weeds.json')
  json_str = json.dumps(config)
  with open(file_path, 'w+') as json_file:
    json_file.write(json_str)


def load_config():
  if has_config():
    file_path = Path('weeds.json')
    with open(file_path, 'r') as json_file:
      config = json.load(json_file)
      return config
  else:
      return None


def has_w(config, path):
  for w in config['weeds']:
    if w['path'] == path:
      return True
  
  return False