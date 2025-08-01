from pathlib import Path
from typing import Any

import streamlit as st
import streamlit.components.v1 as components

# Tell streamlit that there is a component called streamlit_social_share,
# and that the code to display that component is in the "frontend" folder
frontend_dir = (Path(__file__).parent / "frontend").absolute()
_component_func = components.declare_component(
	"streamlit_social_share", path=str(frontend_dir)
)

# Create the python function that will be called
def streamlit_social_share(
    text: str = "",
    url: str | None = None,
    image: str | None = None,
    networks: list[str] | None = None,
    key: str | None = None,
) -> Any:
    """Display social sharing buttons in a Streamlit app.

    Parameters
    ----------
    text : str, optional
        Text to include in the shared message, by default an empty string.
    url : str | None, optional
        The URL to share. If ``None``, the current page URL is used.
    image : str | None, optional
        Image to attach to the share when supported.
    networks : list[str] | None, optional
        Social networks to display. If ``None``, all default networks are shown.
    key : str | None, optional
        An optional unique key to identify the component.

    Returns
    -------
    Any
        The name of the network used for sharing or ``None`` if no share was
        performed.
    """
    component_value = _component_func(
        text=text,
        url=url,
        image=image,
        networks=networks,
        key=key,
    )

    return component_value


def main():
    st.write("## Example")
    value = streamlit_social_share()

    st.write(value)


if __name__ == "__main__":
    main()
