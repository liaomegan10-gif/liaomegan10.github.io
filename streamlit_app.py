import streamlit as st

st.set_page_config(
    page_title="Care Companion",
    page_icon="💙",
    layout="wide",
)
 
# Sidebar navigation
st.sidebar.title("💙 Care Companion")
page = st.sidebar.radio(
    "Navigation",
    ["Dashboard", "Add a Task", "About"],
)

if page == "Dashboard":
    st.title("Your Care Dashboard")
    st.write("Welcome back! Here's your overview.")

    # Three dashboard columns
    col1, col2, col3 = st.columns(3)

    col1.metric("Tasks Today", 5)
    col2.metric("Completed", 3)
    col3.metric("Remaining", 2)

    st.subheader("Today's Priorities")
    st.info("Morning medication reminder")
    st.success("Appointment confirmed")

elif page == "Add a Task":
    st.title("Add a Care Task")

    with st.form("task_form"):
        task = st.text_input("Task name")
        due_date = st.date_input("Due date")
        notes = st.text_area("Additional notes")

        submitted = st.form_submit_button("Save Task")

    if submitted:
        if task.strip():
            st.success(f"Task added: {task}")
            st.write("Due date:", due_date)
            if notes:
                st.write("Notes:", notes)
        else:
            st.warning("Please enter a task name.")

else:
    st.title("About Care Companion")
    st.write("A simple tool to help organize care tasks.")
