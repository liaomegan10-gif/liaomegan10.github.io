import streamlit as st

st.set_page_config(
    page_title="Health Translation",
    page_icon="🫀",
    layout="wide",
)
st.markdown('<style>[data-testid="stSidebar"] label p {font-size: 24px !important;}</style>', unsafe_allow_html=True)
# Sidebar navigation
st.sidebar.title("Healthcare Translator")
page = st.sidebar.radio(
    "Navigation",
    ["Chat", "History", "Basic Life Support"],
)

if page == "Chat":
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
    
    import requests
    
    st.set_page_config(page_title="AI Chatbot", page_icon="🤖")
    
    st.title("🤖 My AI Chatbot")
    st.caption("Powered by Ollama")
    
    # Load your API key from Streamlit Secrets
    try:
        api_key = st.secrets["OLLAMA_API_KEY"]
    except (KeyError, FileNotFoundError):
        st.error(
            "API key not configured. Add OLLAMA_API_KEY "
            "in your Streamlit app's Secrets settings."
        )
        st.stop()
    
    # Keep messages during this browser session
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {
                "role": "assistant",
                "content": "Hi! What can I help you with?"
            }
        ]
    
    # Display conversation
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    # Receive user input
    if prompt := st.chat_input("Ask me anything..."):
        st.session_state.messages.append(
            {"role": "user", "content": prompt}
        )
    
        with st.chat_message("user"):
            st.markdown(prompt)
    
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                try:
                    response = requests.post(
                        "https://ollama.com/api/chat",
                        headers={
                            "Authorization": f"Bearer {api_key}",
                            "Content-Type": "application/json",
                        },
                        json={
                            # Use a model available to your Ollama account.
                            "model": "gemma4:31b",
                            "messages": st.session_state.messages,
                            "stream": False,
                        },
                        timeout=120,
                    )
    
                    response.raise_for_status()
                    answer = response.json()["message"]["content"]
                    st.markdown(answer)
    
                    st.session_state.messages.append(
                        {"role": "assistant", "content": answer}
                    )
    
                except requests.exceptions.RequestException:
                    st.error(
                        "Could not reach Ollama. Check your internet "
                        "connection, API key, model access, and usage limits."
                    )
                except (KeyError, ValueError):
                    st.error("Ollama returned an unexpected response.")


elif page == "History":
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

elif page == "Basic Life Support":
    st.title("Basic Life Support Trainings")

    if st.button("Tourniquet tying"):
        show_page2()
    
    if st.button("Narcan Training"):
        show_page3()

elif page == "Tourniquet Tying":
    st.title("Tourniquet Tying Step By Step")
