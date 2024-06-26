import streamlit as st
import hashlib
from role import Role
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def set_page(page_name):
    st.session_state['current_page'] = page_name
    st.rerun()

def select_role():
    role_option = st.sidebar.radio("Select your role:", ("Developer", "Consumer"))
    st.session_state.responselength = st.sidebar.number_input(
        "Set the AI response word count", 
        min_value=10, 
        max_value=600, 
        value=200,
        step=5
    )
    if role_option == "Developer":
        st.session_state.role = st.session_state.DEVELOPER_ROLE
    else:
        st.session_state.role = st.session_state.CONSUMER_ROLE

def addFromPlayground(query,text_response,entries):
    for entry in entries:
        st.session_state.role.chat.history.append(entry)
    st.session_state.messages[st.session_state.role.name].append(
        {
            "role":"user",
            "content": query
        }
    )
    st.session_state.messages[st.session_state.role.name].append(
        {
            "role":"assistant",
            "content":text_response
        }
    )


