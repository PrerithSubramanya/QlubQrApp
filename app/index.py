import pynecone as pc
from app.state_utils import State
from app.s3_utils import get_s3_resource


def get_s3_objects() -> list:
    s3 = get_s3_resource()
    my_bucket = s3.Bucket("qlubqrapp")
    return [obj.key.strip(".png") for obj in my_bucket.objects.all()]


def restaurant_logo() -> pc.box:
    return pc.box(
        pc.image(
            src="https://qlub-cloud.s3.ap-southeast-1.amazonaws.com/temp/112022/lb3mq705ebfrdrrgddp_Malabar%20Darlinghurst%20Logo.png",
            width="100px",
            height="auto",
        )
    )


def table_design(name: str) -> pc.box:
    return pc.box(
        pc.button(
            name,
            on_click=[
                State.set_table_name,
                State.process_image,
                State.get_image,
                State.modal_change,
            ],
        ),
        pc.cond(
            State.image_processing,
            pc.cond(
                State.image_made,
                pc.modal(
                    pc.modal_overlay(
                        pc.modal_content(
                            pc.modal_header(name),
                            pc.modal_body(
                                pc.image(
                                    src=State.image_url,
                                    height="10em",
                                    width="10em",
                                )
                            ),
                            pc.modal_footer(
                                pc.button(
                                    "Close",
                                    on_click=[State.modal_change, State.process_image],
                                )
                            ),
                        ),
                    ),
                    is_open=State.modal_show,
                    is_centered=True,
                ),
            ),
        ),
        bg="white",
        padding="2em",
        shadow="lg",
        border_radius="lg",
    )


def table_layouts():
    list_tables = get_s3_objects()
    return pc.responsive_grid(
        table_design(list_tables[0]),
        table_design(list_tables[1]),
        table_design(list_tables[2]),
        table_design(list_tables[3]),
        table_design(list_tables[4]),
        table_design(list_tables[5]),
        columns=[3],
        spacing="4",
    )


# noinspection PyCallingNonCallable
def index():
    return pc.center(
        pc.vstack(
            restaurant_logo(),
            table_layouts(),
        ),
        width="100%",
        height="100vh",
        bg="#7d00d4",
    )
