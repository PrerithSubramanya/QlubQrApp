import pynecone as pc
from app import styles
from app.state_utils import State


def custom_container():
    return pc.vstack(
        pc.image(
            src=styles.QLUB_LOGO,
            width="100px",
            height="auto",
        ),
        pc.select(
            State.table_list,
            on_click=State.get_table_list,
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
    )


def main_container():
    return pc.center(
        custom_container(),
        width="100%",
        height="100vh",
        bg="#4158D0",
        background_image="linear-gradient( 83.2deg,  rgba(150,93,233,1) 10.8%, rgba(99,88,238,1) 94.3% )",
    )


def landing():
    return pc.center(
        pc.vstack(
            pc.text(
                "Welcome To",
                font_size=styles.HERO_FONT_SIZE,
                font_weight=styles.DOC_HEADING_FONT_WEIGHT,
                font_family=styles.TEXT_FONT_FAMILY,
                background_image="linear-gradient(271.68deg, #EE756A 25%, #756AEE 50%)",
                background_clip="text",
            ),
            pc.box(
                pc.image(
                    src=styles.QLUB_LOGO,
                    width="250px",
                    height="auto",
                )
            ),
            pc.text(
                "Qr App",
                font_size=styles.HERO_FONT_SIZE,
                font_weight=styles.DOC_HEADING_FONT_WEIGHT,
                font_family=styles.TEXT_FONT_FAMILY,
                background_image="linear-gradient(271.68deg, #EE756A 25%, #756AEE 50%)",
                background_clip="text",
            ),
            pc.text(
                "Generate Qr code digitally.",
                color="grey",
                font_size="1.1em",
                font_family=styles.TEXT_FONT_FAMILY,
                text_align="center",
            ),
        ),
        width="100%",
        height="100vh",
        background_image="linear-gradient( 174.2deg,  rgba(255,244,228,1) 7.1%, rgba(240,246,238,1) 67.4% )",
    )


def restaurants():
    return main_container()
