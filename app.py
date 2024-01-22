from openai_functions import analyze_image_basic,generate_with_response_model
from prompt_template import anlysis_prompt
from ai_personas import persona_prompts_small,persona_prompts_big
from models import SuggestionsModel
import web_screenshot

url = "https://learnwithhasan.com"

captured_image_path = web_screenshot.capture_web_page_image(url,"screenshot_test.jpg")
image_url = web_screenshot.upload_to_imgur(captured_image_path)

# Initialize an empty list to store all the results
all_persona_results = []

#loop through the list or personas and ask for evaluation
for persona in persona_prompts_small:
    for title, prompt in persona.items():
        print(f"Analyzing With: {title}...")
        persona_prompt = f"{prompt} {anlysis_prompt}"
        result = analyze_image_basic(image_url,persona_prompt)
        all_persona_results.append(result)
        print("Done------")

#get  the overaall results
results_string = '\n'.join(all_persona_results)
final_prompt = f"Act as a Landing Page Expert Analyzer, please checkout the following feedback from different people about a landing page, extract 7-10 unique suggestions, and return them in a list in JSON format. Feedback: {results_string}"
overall_analysis = generate_with_response_model(final_prompt,SuggestionsModel)
print(overall_analysis.result)

