# streamlit-social-share

Streamlit component that allows you to share your data via the native browser functionality

## Installation instructions 

```sh
pip install streamlit-social-share
```

## Usage instructions

```python
import streamlit as st

from streamlit_social_share import streamlit_social_share

value = streamlit_social_share()

st.write(value)
```

By default the component shares the current page URL and shows buttons for all
available networks. The function returns the name of the network the user chose
to share with, or ``None`` if no action was taken.
