import configparser


def generate_global_config():
    config = configparser.ConfigParser()
    config["common"] = {'Bot_ip': "127.0.0.1",
                        "qq": 123456,
                        "superAdmin": 123456,
                        'Bot_port': 8888,
                        'wakada_token': False
                        }
    with open("config.ini", "w") as f:
        config.write(f)



def generate_group_config(config_name):
    config = configparser.ConfigParser()
    config["common"] = {'enableBot': True,
                        'SuperAdmin': ctx.FromUin,
                        'enableLoli': False,
                        'enableWsg': False
                        }
