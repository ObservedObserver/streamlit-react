import streamlit as st

def get_context():
    if (st.session_state.get("_st_react_context", None) is None):
        st.session_state["_st_react_context"] = {
            "current_element": None,
        }
    ctx = st.session_state.get("_st_react_context")
    return ctx