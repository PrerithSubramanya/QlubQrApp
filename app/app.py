import pynecone as pc
from app.state_utils import State
from app.index import index

app = pc.App(state=State)
app.add_page(index, title="QlubQrApp")
app.compile()
