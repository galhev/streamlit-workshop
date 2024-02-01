from st_pages import Page, Section, show_pages, add_page_title

import plotly.express as px
import streamlit as st
from datasets import load_dataset
import pandas as pd

st.title('🤓 Streamlit Workshop 😎')
show_pages(
    [
        Page("app.py", "Info", "🧙"),
        # Workshop
        Page("pages/tabs.py", "Tabs", "💻", in_section=True),
        Page("pages/background.py", "Background", "📚", in_section=True),
        Page("pages/dropdown.py", "Dropdown", "📝",
             in_section=True),
    ]
)



st.markdown("### 👨‍🔧 Fun Plotly & Streamlit Workshop by [Gal Hever](https://www.linkedin.com/in/gal-hever/)")

st.image("https://upload.wikimedia.org/wikipedia/commons/7/77/Streamlit-logo-primary-colormark-darktext.png")

st.info("For the full code go to the repository on [Github](https://github.com/galhev)")

st.markdown("---")

with st.expander("So what we are going to do today?"):
    st.markdown("""

    <a href="https://www.youtube.com/watch?v=__fwMqh-2WA"><img src="https://lordicon.com/icons/wired/lineal/2507-learn-more-text.svg" height="50" /></a>

    #

    - For more info about [streamlit](https://streamlit.io/)
    - Join the [Streamlit Course in Udemy](https://www.udemy.com/course/learn-streamlit-python/?utm_source=adwords&utm_medium=udemyads&utm_campaign=LongTail_la.EN_cc.ROW&utm_content=deal4584&utm_term=_._ag_77879424134_._ad_535397245863_._kw__._de_c_._dm__._pl__._ti_dsa-1007766171312_._li_20517_._pd__._&matchtype=&gad_source=1&gclid=Cj0KCQiAh8OtBhCQARIsAIkWb686bS0WTgx9S3_iisbEiPvV1VmtKpZnAV7kPebN4Fi_MzBpUbLElHoaAuRGEALw_wcB)    - Join the [course Telegram channel with announcements](https://t.me/dezoomcamp)
    - Join the [Streamlit Community](https://discuss.streamlit.io/t/welcome-to-the-streamlit-community/7#questions-thinkingface_with_monocle-2)

    #""", unsafe_allow_html=True)

st.markdown("---")

st.markdown("""
    ### ⭐ Star the project on <a href="https://github.com/galhev"><img src="https://miro.medium.com/v2/resize:fit:1125/1*wotzQboYWAfaj-7bvGNIkQ.png" height="50" /></a>

""", unsafe_allow_html=True)
