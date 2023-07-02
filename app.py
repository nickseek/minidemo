import streamlit as st
from generate import Generator

generator = Generator()

def main():
   
    st.title("Prompt Submission")
    
    # Text input field
    user_input = st.text_area("Enter Prompt")

    # Submit button
    if st.button("Submit"):
        # Process the submitted text
        processed_text = generator.generate_text(user_input)
        # Display the processed text
        st.subheader("Model generation:")
        st.title(processed_text)
        

if __name__ == "__main__":
    main()





