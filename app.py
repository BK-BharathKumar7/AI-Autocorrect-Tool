import streamlit as st
import language_tool_python

# Initialize LanguageTool
tool = language_tool_python.LanguageTool('en-US')

st.set_page_config(page_title="AI Autocorrect Tool")

st.title("AI-Powered Autocorrect Tool")
st.write("Correct spelling and grammar mistakes automatically.")

user_text = st.text_area("Enter your text:", height=200)

if st.button("Correct Text"):
    
    if user_text.strip():
        
        # Find mistakes
        matches = tool.check(user_text)

        # Correct text
        corrected_text = language_tool_python.utils.correct(
            user_text,
            matches
        )

        st.subheader("Original Text")
        st.write(user_text)

        st.subheader("Corrected Text")
        st.success(corrected_text)

        st.subheader("Statistics")
        st.write(f"Total Issues Found: {len(matches)}")

        if matches:
            st.subheader("Detected Issues")

            for i, match in enumerate(matches, start=1):
                st.write(f"**Issue {i}:** {match.message}")

                if match.replacements:
                    st.write(
                        f"Suggested Correction: {match.replacements[0]}"
                    )

                st.write("---")

        st.download_button(
            label="Download Corrected Text",
            data=corrected_text,
            file_name="corrected_text.txt",
            mime="text/plain"
        )

    else:
        st.warning("Please enter some text.")
