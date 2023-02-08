import os
import pynecone as pc
from pynecone import utils

config = pc.Config(
    app_name="app",
    api_url="https://mighty-cliffs-67168.herokuapp.com:8000",
    env=pc.Env.PROD,
    port=os.environ["PORT"],
)


initial_get_api_port = utils.get_api_port


def patched_get_api_port() -> int:
    print("Using patched get_api_port (return 8000)")
    return 8000


utils.get_api_port = patched_get_api_port
print("Patched 'get_api_port' to always return 8000.")
