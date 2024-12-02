import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] +  "\n"
    todos.append(todo)
    functions.write_todos(todos)


st.title("My Todo App")
#sub-header
st.subheader("This is my todo app")
#write text
st.write("This app is to improve your productivity")

 #put a checkbox
# st.checkbox("Buy groceries")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="", placeholder="Enter a new todo....",
              on_change=add_todo, key='new_todo')
