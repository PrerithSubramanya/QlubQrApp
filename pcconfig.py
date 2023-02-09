import os
import pynecone as pc
from pynecone import utils

config = pc.Config(
    app_name="app",
    api_url="0.0.0.0:8000",
    bun_path="/app/.bun/bin/bun",
)
