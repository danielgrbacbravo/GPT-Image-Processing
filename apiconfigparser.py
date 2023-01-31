import configparser

config = configparser.ConfigParser()
import os

def  create_config():
    print('example.ini does not exist, creating file')
    config['API-KEYS'] = {'OPENAI_API_KEY': '<api-key>'}

    with open('example.ini', 'w') as configfile:
        config.write(configfile)

# if example.ini does not exist in working directory run create_config() 
if not os.path.exists("example.ini"):
    create_config()
else:
    config.read('example.ini')
    config.sections()
    print(config['API-KEYS']['openai_api_key'])
# if example.ini exists run 

def get_openai_api_key():
    if not os.path.exists("example.ini"):
        create_config()
        return 
    else:
        config.read('example.ini')
        config.sections()
        return config['API-KEYS']['openai_api_key']