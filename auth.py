from utils import hash_password
import sqlite3
import streamlit as st

def createSession(username,allowedRetries,summaryRetries):
    st.session_state['user_authenticated'] = True
    st.session_state['username'] = username
    st.session_state.summaryFree=int(summaryRetries)
    st.session_state.searchFree=int(allowedRetries)
    st.session_state.cookies["logged_in"]="true"
    st.session_state.cookies["username"]=username
    st.session_state.cookies["summaryFree"]=str(summaryRetries)
    st.session_state.cookies["searchFree"]=str(allowedRetries)

def create_user(usernamer, passwordr, emailr, paid=0):
    conn=sqlite3.connect('users.db')
    c = conn.cursor()
    allowedRetries=1000 if paid==1 else 7
    summaryRetries=1000 if paid==1 else 7
    try:
        c.execute('INSERT INTO users (username, password, email, searchRetries, summaryRetries) VALUES (?,?,?,?,?)',(usernamer,hash_password(passwordr),emailr,allowedRetries,summaryRetries));
        conn.commit();
        st.success('User created. Signing in...')
        createSession(usernamer,allowedRetries,summaryRetries)
    except Exception as e:
        return False
    finally:
        conn.close()
    return True

def authenticate_user(username, password):
    conn=sqlite3.connect('users.db')
    c=conn.cursor()
    c.execute('SELECT password, searchRetries, summaryRetries FROM users WHERE username = ?', (username,))
    result = c.fetchone()
    conn.close()
    if result and result[0] == hash_password(password):
        password, allowedRetries, summaryRetries = result
        createSession(username,allowedRetries,summaryRetries)
        return True
    return False

def update_user(username):
    conn=sqlite3.connect('users.db')
    c=conn.cursor()
    try:
        c.execute('UPDATE users set searchRetries=?,summaryRetries=? where username=?',(st.session_state.searchFree,st.session_state.summaryFree,username));
        conn.commit();
    except Exception as e:
        print(e)
        return False
    finally:
        conn.close()
    return True

def check_duplicate(username):
    conn=sqlite3.connect('users.db')
    c=conn.cursor()
    c.execute('SELECT username FROM users WHERE username = ?', (username,))
    result = c.fetchone()
    conn.close()
    if result:
        return True
    return False

def get_comments(offset=0, limit=10):
    conn=sqlite3.connect('users.db')
    cursor=conn.cursor()
    cursor.execute("SELECT username, created_at, comment FROM comments ORDER BY created_at DESC LIMIT ? OFFSET ?", (limit, offset))
    comments = cursor.fetchall()
    conn.close()
    return comments

def add_comment(username, comment):
    conn=sqlite3.connect('users.db')
    cursor=conn.cursor()
    cursor.execute("INSERT INTO comments (username, comment) VALUES (?, ?)", (username, comment))
    conn.commit()
    conn.close()

