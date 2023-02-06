import pynecone as pc
from QlubApp.state_utils import State
from QlubApp.index import index

app = pc.App(state=State)
app.add_page(index)
app.compile()
