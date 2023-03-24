import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state['new_todo'] + '\n'
    todos.append(todo)
    functions.write_todos(todos)

st.title('My Todo App')
st.subheader('This is my todo app')
st.write("this app is used for increase in producitivity")

for todo in todos:
    st.checkbox(todo)

st.text_input(label='', placeholder='Add new todo . . .',
              key='new_todo',on_change=add_todo)

st.session_state
