import streamlit as st
import google.generativeai as genai


AVAILABLE_MODELS = {
    "Gemini 1.5 Pro (Best quality)": "models/gemini-1.5-pro-latest",
    "Gemini 1.5 Flash (Faster & cheaper)": "models/gemini-1.5-flash-latest",
    "Gemini 1.5 Pro (v002)": "models/gemini-1.5-pro-002"
}


def configure_genai():
    api_key = st.secrets["GEMINI_API_KEY"]["key"]
    if not api_key:
        st.error("API key not found. Please configure the secrets.toml file.")
        st.stop()
    genai.configure(api_key=api_key)


def generate_startup_plan(problem, industry, audience, budget, model_name):
    model = genai.GenerativeModel(model_name)

    prompt = f"""
    Create a comprehensive startup plan based on the following inputs:
    - Problem: {problem}
    - Industry: {industry}
    - Target Audience: {audience}
    - Budget: {budget}

    The plan should include:
    1. Startup Name (creative and memorable)
    2. Value Proposition (clear statement of value)
    3. Target Market (detailed description)
    4. Revenue Model (how it will make money)
    5. Key Features (main product/service features)
    6. Competitive Advantage (what makes it unique)
    7. Initial Steps (first actions to take)

    Format the output in clear markdown with headings for each section.
    """

    response = model.generate_content(prompt)
    return response.text

# Here, the main function starts. I have provided 5 options, and we can also select the model. The models are listed above targeted under the name 'AVAILABLE MODELS' 
def main():
    st.set_page_config(page_title="Startup Generator", layout="wide")
    st.title("AI-Powered Startup Idea Generator")

    with st.form("startup_inputs"):
        problem = st.text_area("Describe the problem you're trying to solve:")
        industry = st.text_input("Industry/Domain (e.g., Healthcare, Education):")
        audience = st.text_input("Target Audience (optional):")
        budget = st.selectbox("Budget Range (optional):", ["", "< $10k", "$10k-$50k", "$50k-$100k", ">$100k"])
        model_choice = st.selectbox("Choose Gemini Model", list(AVAILABLE_MODELS.keys()))

        submitted = st.form_submit_button("Generate Startup Plan")

        if submitted:
            if not problem:
                st.warning("Please describe the problem you're trying to solve.")
            else:
                with st.spinner("Generating your startup plan..."):
                    try:
                        configure_genai()
                        plan = generate_startup_plan(
                            problem, industry, audience, budget,
                            AVAILABLE_MODELS[model_choice]
                        )
                        st.markdown(plan)
                    except Exception as e:
                        st.error(f"Error generating plan: {e}")

    st.markdown("---")
    st.caption("Developed by Ramsha Noshad for National Incubation Center")

if __name__ == "__main__":
    main()
