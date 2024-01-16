from typing import List
from pydantic import BaseModel
from openai_vision import analyze_image_basic,generate_with_response_model
from prompt_template import anlysis_prompt

class SuggestionsModel(BaseModel):
    result: List[str]

# Personas and their prompts
persona_prompts = [
    {"Young Entrepreneur": "As a young, tech-savvy entrepreneur interested in the latest market trends and innovations, "},
    {"College Student": "As a computer science student with interests in gaming and social media, "},
    {"Freelance Graphic Designer": "As a freelance graphic designer, "},
    {"Corporate Executive": "As a busy corporate executive, "},
    {"Small Business Owner": "As a small business owner of a local café, "},
    {"Professional Blogger": "As a professional blogger, "},
    {"Travel Enthusiast": "As a travel enthusiast, "},
    {"Software Developer": "As a software developer, "},
    {"Fashion Influencer": "As a fashion influencer, "},
    {"Senior Research Scientist": "As a senior research scientist, "},
    {"Digital Nomad": "As a digital nomad who travels while working remotely, "},
    {"Art Student": "As an art student, "},
    {"Digital Marketing Expert": "As a digital marketing expert with a strong background in SEO, PPC, and social media advertising, "}
]

image_url = "https://static.semrush.com/blog/uploads/media/ed/9b/ed9b42a338de806621bdaf70293c2e7e/image.png"
#prompt = f"As a young, tech-savvy entrepreneur interested in the latest market trends and innovations,  {anlysis_prompt}"


# Initialize an empty list to store all the results
all_results = []


#Example of how to loop through the list and print each prompt
for persona in persona_prompts:
    for title, prompt in persona.items():
        persona_prompt = f"{prompt} {anlysis_prompt}"
        result = analyze_image_basic(image_url,persona_prompt)
        all_results.append(result)



results_string = '\n'.join(all_results)
final_prompt = f"Act as a Landing Page Expert Analyzer, please checkout the following feedback from different people about a landing page, extraact the top 10 unique suggestions, and returm them in a list in json format. feedback: {results_string}"
overall_analysis = generate_with_response_model(final_prompt,SuggestionsModel)
print (overall_analysis.result)

