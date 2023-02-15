import pynecone as pc
from app import styles
from app.state_utils import State
from app.index import landing, restaurants

app = pc.App(state=State, stylesheet=styles.STYLESHEETS)
app.add_page(landing, route="", title="QlubQrApp")
app.add_page(restaurants, route="/[name]")

app.compile()
