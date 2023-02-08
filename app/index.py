import pynecone as pc
from app.state_utils import State
from app.s3_utils import get_s3_resource


def get_s3_objects() -> list:
    s3 = get_s3_resource()
    my_bucket = s3.Bucket("qlubqrapp")
    return [obj.key for obj in my_bucket.objects.all()]


# noinspection PyCallingNonCallable
def index():
    return pc.center(
        pc.vstack(
            pc.image(
                src="https://qlub.io/wp-content/uploads/2022/11/logo.svg",
                width="100px",
                height="auto",
            ),
            pc.select(
                get_s3_objects(),
                placeholder="Select a table",
                on_change=State.set_table_name,
            ),
            pc.button(
                "Generate QR",
                on_click=[State.process_image, State.get_image],
                width="100%",
                bg="#7d00d4",
                color="white",
            ),
            pc.divider(),
            pc.cond(
                State.image_processing,
                pc.circular_progress(is_indeterminate=True),
                pc.cond(
                    State.image_made,
                    pc.image(
                        src=State.image_url,
                        height="10em",
                        width="10em",
                    ),
                ),
            ),
            bg="white",
            padding="2em",
            shadow="lg",
            border_radius="lg",
        ),
        width="100%",
        height="100vh",
        bg="#7d00d4",
    )
