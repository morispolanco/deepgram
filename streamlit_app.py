
import streamlit as st

# Assuming the Python functions are already defined as specified in previous instructions

# Initialize session state for story paragraphs
if 'story_paragraphs' not in st.session_state:
    st.session_state['story_paragraphs'] = []

# Streamlit app layout
st.title("Story Generator")

# Sidebar for author style and story subject
author_style = st.sidebar.text_input("Author's Style", value="Hemingway")
story_subject = st.sidebar.text_input("Subject of the Story")

# Start story button
if st.button("Start Story"):
    # Call the Python function to start a new story
    st.session_state['story_paragraphs'] = [start_new_story(author_style, story_subject)]

# Continue story button
if st.button("Continue"):
    # Call the Python function to continue the story
    new_paragraph = continue_story(author_style)
    st.session_state['story_paragraphs'].append(new_paragraph)

# Change last paragraph button
if st.button("Change"):
    # Call the Python function to change the last paragraph
    changed_paragraph = change_last_paragraph(author_style)
    if st.session_state['story_paragraphs']:
        st.session_state['story_paragraphs'][-1] = changed_paragraph

# Finish story button
if st.button("Finish"):
    # Call the Python function to finish the story
    conclusion = finish_story(author_style)
    st.session_state['story_paragraphs'].append(conclusion)

# Display the story
story_text = "\n\n".join(st.session_state['story_paragraphs'])
st.text_area("Story", story_text, height=300)

# Copy to clipboard button (Streamlit does not support clipboard operations directly)
# This button will download the story as a text file
if st.button("Copy"):
    st.download_button('Download Story', story_text, file_name='story.txt')
