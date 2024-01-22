# First, import necessary libraries including Streamlit, and other dependencies from the provided script.
import streamlit as st
from openai_functions import analyze_image_basic, generate_with_response_model
from prompt_template import anlysis_prompt
from ai_personas import persona_prompts_small,persona_prompts_big
from models import SuggestionsModel
import web_screenshot

# Start the Streamlit app
def main():
    # Set the title of the app
    st.title("Landing Page Analyzer")

    # Provide an introduction or instructions for the user
    st.write("Welcome to the Landing Page Analyzer. Please provide an image of a landing page in one of the following ways for analysis.")

    # Option for users to select the method of providing the image
    method = st.radio("Choose your method to provide the image:",
                      ('Public URL', 'URL to Capture'))

    # Initialize a variable for the image URL
    image_url = None

    # Depending on the method chosen, provide different input options
    if method == 'Public URL':
        # Input for public URL
        public_url = st.text_input("Enter the public URL of the image:")
        if public_url:
            image_url = public_url

    elif method == 'URL to Capture':
        # Input for URL to capture
        capture_url = st.text_input("Enter the URL to capture the webpage:")
        if capture_url:
            # Capture the webpage as an image
            captured_image_path = web_screenshot.capture_web_page_image(capture_url, "screenshot_test.jpg")
            image_url = web_screenshot.upload_to_imgur(captured_image_path)

    # Button to start analysis
    if st.button("Analyze Image") and image_url:
        # Call the function to analyze the image
        analyze_image(image_url)

# Function to analyze the image
def analyze_image(image_url):
    # Initialize an empty list to store all the results
    all_persona_results = []

    # Loop through the list of personas and ask for evaluation
    for persona in persona_prompts_small:
        for title, prompt in persona.items():
            st.write(f"Persona: {title}, Analyzing...")
            persona_prompt = f"{prompt} {anlysis_prompt}"
            result = analyze_image_basic(image_url, persona_prompt)
            all_persona_results.append(result)

    # Get the overall results
    results_string = '\n'.join(all_persona_results)
    final_prompt = f"Act as a Landing Page Expert Analyzer, please checkout the following feedback from different people about a landing page, extract 7-10 unique suggestions, and return them in a list in JSON format. Feedback: {results_string}"
    overall_analysis = generate_with_response_model(final_prompt, SuggestionsModel)
    st.write("Overall Analysis:")
    st.json(overall_analysis.result)

# Run the main function when the script is executed
if __name__ == "__main__":
    main()
