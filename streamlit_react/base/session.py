import streamlit as st

def init_session(key: str, default_value=None):
    if st.session_state.get(key) is None:
        st.session_state[key] = default_value
    return st.session_state[key]

def init_element_state(key: str, default_value=None):
    if st.session_state.get('_st_react_state') is None:
        st.session_state['_st_react_state'] = {}
    if st.session_state['_st_react_state'].get(key) is None:
        st.session_state['_st_react_state'][key] = default_value
    return st.session_state['_st_react_state'][key]