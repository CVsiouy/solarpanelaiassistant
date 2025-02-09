import streamlit as st

st.set_page_config(
    page_title="Some AI website",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

chatbot_page = st.Page(
    page = "views/chatbot.py",
    title = "Chatbot",
    icon = ":material/smart_toy:",
    default = True,
)

insights_page = st.Page(
    page = "views/insights.py",
    title = "Insights",
    icon = ":material/bar_chart:",
)

latest_news_page = st.Page(
    page = "views/latestNews.py",
    title = "Latest News",
    icon = ":material/account_circle:",
)


# pg = st.navigation(pages = [chatbot_page, insights_page, latest_news_page ])

pg = st.navigation({
    "Your Personalized Dashboard" : [chatbot_page, insights_page, latest_news_page ],
})


st.logo("assets/my_logo.jpg")
st.sidebar.text("Made with ❤️ in India")
pg.run() 






    


    