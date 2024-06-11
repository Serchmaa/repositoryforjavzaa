import os
from pathlib import Path


def set_env_variables(file_path='env.txt'):
    # We only need to configure environment variable when we running code on the local
    # If file doesn't exist, it means it is running on the github.
    # So in this case, we don't need to configure environment variable.
    # It has already configured in yml file.
    if Path(file_path).is_file():
        with open(file_path, 'r') as file:
            for line in file:
                line = line.strip()
                key, value = line.split('=', 1)
                if value.startswith('"') and value.endswith('"'):
                    value = value[1:-1]
                os.environ[key] = value


# Set the environment variables
set_env_variables()
