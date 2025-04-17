import streamlit as st
import os
from code_editor import code_editor
import traceback
from pathlib import Path
from questions.question_1.test_cases import TEST_CASES
from utils.utility_functions import save_user_code
st.set_page_config(layout="wide")
# -----------------------------
# Custom Styling to Widen Sidebar and Wrap Text
# -----------------------------
st.markdown("""
    <style>
        section[data-testid="stSidebar"] {
            width: 700px !important;
            min-width: 700px !important;
            max-width: 700px !important;
            flex-shrink: 0 !important;
        }
        section.main {
            margin-left: 420px;
        }
        .ace_content {
            white-space: pre-wrap !important;
            word-wrap: break-word !important;
        }
        .ace_text-layer {
            white-space: pre-wrap !important;
        }
        .ace_scrollbar-h {
            display: none !important;
        }
    </style>
""", unsafe_allow_html=True)

# -----------------------------
# Sidebar Problem Description
# -----------------------------
question_path = os.path.join(os.path.dirname(__file__), "questions", "question_1", "question_1.md")
try: 
    with open(question_path, "r") as f:
        question_text = f.read()
    st.sidebar.markdown(question_text)
except FileNotFoundError:
    st.sidebar.error(f"⚠️ Question file not found at {question_path}")

# -----------------------------
# Default Code and Completion List
# -----------------------------
default_code = """
from typing import List, Dict

def filter_and_sort_symptoms(symptoms: List[Dict[str, int | str]]) -> List[str]:
    # Your code here
    return []
"""

saved_code = default_code

completions = [
    {"caption": "filter_and_sort_symptoms", "value": "filter_and_sort_symptoms", "meta": "function"},
    {"caption": "symptoms", "value": "symptoms", "meta": "variable"},
    {"caption": "severity", "value": "severity", "meta": "key"},
    {"caption": "frequency", "value": "frequency", "meta": "key"},
    {"caption": "sorted", "value": "sorted", "meta": "builtin"},
]

editor_buttons = [
    {
        "name": "Run",
        "feather": "Play",
        "primary": True,
        "hasText": True,
        "showWithIcon": True,
        "commands": ["submit"],
        "style": {"bottom": "0.44rem", "right": "0.4rem"},
    }
]

# -----------------------------
# Test Case Setup
# -----------------------------
st.title("💻 Coding Challenge")
info_bar = []

symptoms_input = [
    {"name": "headache", "severity": 7, "frequency": 5},
    {"name": "fatigue", "severity": 3, "frequency": 2},
    {"name": "nausea", "severity": 5, "frequency": 5},
    {"name": "dizziness", "severity": 4, "frequency": 3},
    {"name": "blurred vision", "severity": 2, "frequency": 6}
]

expected_output = ["headache", "nausea", "dizziness"]

if "submitted_code" not in st.session_state:
    st.session_state["submitted_code"] = None

if "code_editor_text" not in st.session_state:
    st.session_state["code_editor_text"] = saved_code

# -----------------------------
# Render Initial Editor
# -----------------------------
editor_response = code_editor(
    st.session_state["code_editor_text"],
    lang="python",
    height=[20, 100],
    
    ghost_text="Start writing your solution here...",
    buttons=editor_buttons,
    response_mode=["blur", "debounce", "submit"],
    completions=completions
)

if editor_response and editor_response.get("type") == "submit":
    code_to_run = editor_response["text"]
    st.session_state["submitted_code"] = code_to_run
    st.session_state["code_editor_text"] = code_to_run

if st.session_state["submitted_code"]:
    try:
        code_to_run = st.session_state["submitted_code"]
        local_env = {}
        exec(code_to_run, {}, local_env)

        if "filter_and_sort_symptoms" in local_env:
            func = local_env["filter_and_sort_symptoms"]
            tabs = st.tabs([f"Test Case {i+1}" for i in range(len(TEST_CASES))])
            for i, (tab, case) in enumerate(zip(tabs, TEST_CASES)):
                with tab:
                    try:
                        result = func(case["input"])
                        match = result == case["expected"]
                        if match:
                            st.success(f"✅ Test Case {i+1} Passed")
                            st.subheader("Input")
                            st.json(case["input"])
                            st.subheader("Output")
                            st.json(result)
                        else:
                            st.error(f"❌ Test Case {i+1} Failed")
                            st.subheader("Input")
                            st.json(case["input"])
                            st.subheader("Expected Output")
                            st.json(case["expected"])
                            st.subheader("Received Output")
                            st.json(result)
                    except Exception as e:
                        st.error(f"❌ Error in Test Case {i+1}: {e}")
                        st.subheader("Input")
                        st.json(case["input"])
        else:
            st.error("❌ Function `filter_and_sort_symptoms` not found.")
    except Exception:
        error_message = traceback.format_exc()
        st.error("❌ An error occurred:")
        st.code(error_message)
    

# -----------------------------
# Run Code Logic
# -----------------------------
