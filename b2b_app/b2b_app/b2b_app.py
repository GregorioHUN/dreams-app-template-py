"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from rxconfig import config
from reflex_type_animation import type_animation


class State(rx.State):
    """The app state."""

    ...


def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.box(
	    rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.heading("Welcome to B2B, Judig", size="9"),
            rx.text(
                "Get ready, we're launching soon the alpha version...! "
				# ,rx.code(f"{config.app_name}/{config.app_name}.py")
				,size="7",)
            ,type_animation(
                sequence=["This is an example demo test from Greg", 1000]
            )

			# ,rx.link(
   #               rx.button("Check out our docs!"),
   #               href="https://reflex.dev/docs/getting-started/introduction/",
   #               is_external=True,
   #          )
			,spacing="5",
             justify="center",
             min_height="85vh",
        )
		# ,rx.logo()
		,
    ),
	background="center/cover url('/launching_soon_background_compressed.webp')",
    width="100%",
    height="100vh",
	
	)


app = rx.App()
app.add_page(index)
