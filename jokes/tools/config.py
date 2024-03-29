import yaml


def read_config(file_name):
    # wczytanie konfiguracji
    with open(file_name, "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)

    return config
