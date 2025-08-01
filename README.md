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
