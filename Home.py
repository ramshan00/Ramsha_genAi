import streamlit as st
# WELCOME PAGE 


def main():
    st.set_page_config(page_title="National Incubation Center(NIC) Startup Generator", layout="wide")
    
    st.title("National Incubation Center")
    st.subheader("AI-Powered Startup Idea Generator")
    
    st.markdown("""
    Welcome to the NIC Startup Generator! This tool helps entrepreneurs:
    - Generate innovative startup ideas
    - Develop complete business plans
    - Identify market opportunities
    
    Click below to get started.
    """)
    
    if st.button("Generate Startup Idea"):
        st.switch_page("pages/generator.py")
    
    st.markdown("---")
    st.caption("Developed by RAMSHA NOSHAD for National Incubation Center")

if __name__ == "__main__":
    main()


