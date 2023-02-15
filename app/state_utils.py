import pynecone as pc
from app.s3_utils import get_table_qr_image, get_s3_objects


class State(pc.State):
    """The app state."""

    folder_name: str = ""
    table_name: str = ""
    image_url: str = ""
    image_processing: bool = False
    image_made: bool = False
    table_list: list[str] = []

    @pc.var
    def rest_name(self):
        return self.get_query_params().get("name", "no name")

    def get_table_list(self):
        """Get the table_list on click."""
        self.table_list = get_s3_objects(
            route=self.get_query_params().get("name", "no name")
        )

    def process_image(self):
        """Set the image processing flag to true and indicate image is not made yet."""
        self.image_processing = True
        self.image_made = False

    def get_image(self):
        """Get the image from the prompt."""
        self.image_url = get_table_qr_image(
            folder_name=self.get_query_params().get("name", "no name"),
            table_name=self.table_name,
        )
        self.image_processing = False
        self.image_made = True
