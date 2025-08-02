import streamlit as st

from streamlit_social_share import streamlit_social_share, create_custom_network

st.set_page_config(page_title="Streamlit Social Share Example")

st.write("# 🚀 Streamlit Social Share Demo")

st.markdown("""
This component allows you to easily add social sharing buttons to your Streamlit app. 
Users can share your content across various social media platforms with just one click!

## How to use:
1. **Install the component**: `pip install streamlit-social-share`
2. **Import it**: `from streamlit_social_share import streamlit_social_share, create_custom_network`
3. **Use it**: Add sharing buttons to your app with customizable networks
""")

st.write("## 📱 All Available Networks")

# Networks organized by category and sorted by color (dark to light)
social_media = ["x", "threads", "linkedin", "facebook", "instagram", "reddit"]
messaging = ["signal", "telegram", "whatsapp", "email"]
professional = ["github", "stackoverflow", "youtube"]

all_networks = social_media + messaging + professional

st.write("Click a button below to share!")

network = streamlit_social_share(
    text="Check out this amazing Streamlit Social Share component!",
    url="https://streamlit.io",
    image="https://streamlit.io/images/brand/streamlit-logo-primary-colormark-darktext.png",
    networks=all_networks,
    key="all_networks"
)
    


st.write("## 🛠️ Code Example")

st.write("💡 **Tip**: You can mix built-in networks with your custom ones in the `networks` parameter!")

st.markdown("""
```python
from streamlit_social_share import streamlit_social_share, create_custom_network

# Create custom networks (this registers them globally)
my_platform = create_custom_network(
    network_id="my_platform",
    name="My Platform",
    color="#FF6B6B",
    icon="🚀",  # Can be emoji, character, or URL to image
    share_url="https://myplatform.com/share?url={url}&text={text}"
)

dev_network = create_custom_network(
    network_id="dev_community",
    name="Dev Community",
    color="#4ECDC4",
    icon="👨‍💻",
    share_url="https://dev.to/new?prefill={text} {url}"
)

# Use custom networks alongside built-in ones
streamlit_social_share(
    text="My custom share text",
    url="https://example.com",
    networks=[my_platform, dev_network, "linkedin", "x"]  # Clean and simple!
)
```
""")

# Create custom networks using the new function
my_platform = create_custom_network(
    network_id="my_platform",
    name="My Platform",
    color="#FF6B6B",
    icon="🚀",
    share_url="https://example.com/share?url={url}&text={text}"
)

dev_community = create_custom_network(
    network_id="dev_community", 
    name="Dev Community",
    color="#4ECDC4",
    icon="👨‍💻",
    share_url="https://dev.to/new?prefill={text} {url}"
)

hacker_news = create_custom_network(
    network_id="hacker_news",
    name="Hacker News",
    color="#FF6600",
    icon="📰", 
    share_url="https://news.ycombinator.com/submitlink?u={url}&t={text}"
)

custom_network = streamlit_social_share(
    text="Check out this custom social sharing component!",
    url="https://github.com",
    networks=[my_platform, dev_community, hacker_news, "linkedin", "x"],
    key="custom_networks"
)


st.write("## ⚙️ Parameters")

st.markdown("""
### streamlit_social_share()
| Parameter | Type | Description | Required |
|-----------|------|-------------|----------|
| `text` | str | Text to include in the shared message | No |
| `url` | str | URL to share (defaults to current page) | No |
| `image` | str | Image URL to attach when supported | No |
| `networks` | list[str] | List of network IDs to display | No |
| `key` | str | Unique component key | No |

### create_custom_network()
| Parameter | Type | Description | Required |
|-----------|------|-------------|----------|
| `network_id` | str | Unique identifier for the network | Yes |
| `name` | str | Display name for the button | Yes |
| `color` | str | Background color (hex code) | Yes |
| `icon` | str | Emoji, character, or URL to an image | Yes |
| `share_url` | str | URL template with {text}, {url}, {image} placeholders | Yes |

**Returns:** `str` - The network_id that can be used in the networks parameter
""")
