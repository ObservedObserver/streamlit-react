import streamlit as st
import streamlit_react as sr

st.title("Home")

with sr.element("div", className="rounded-lg p-4 shadow-lg bg-white border"):
    sr.element("h1", "Hello World", className="text-2xl font-bold")
    sr.element("p", "This is a paragraph", className="text-blue-500")