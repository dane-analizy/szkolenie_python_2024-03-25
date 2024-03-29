from tools.db import get_sql_results
from tools.config import read_config

CONFIG_FILE = "config_db.yaml"

config = read_config(CONFIG_FILE)

get_sql_results(config, "DELETE FROM jokes WHERE id > 10;")