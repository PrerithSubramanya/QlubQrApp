import pynecone as pc

config = pc.Config(
    app_name="app",
    api_url="http://qr-app-backend.qlub.cloud",
    # api_url="http://localhost:8000",
    env=pc.Env.PROD,
)
