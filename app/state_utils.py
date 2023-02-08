import pynecone as pc
from app.s3_utils import get_table_qr_image


class State(pc.State):
    """The app state."""

    table_name: str = ""
    image_url: str = ""
    image_processing = False
    image_made = False

    def process_image(self):
        """Set the image processing flag to true and indicate image is not made yet."""
        self.image_processing = True
        self.image_made = False

    def get_image(self):
        """Get the image from the prompt."""
        self.image_url = get_table_qr_image(table_name=self.table_name)
        self.image_processing = False
        self.image_made = True
