import pyperclip

from job_summary_pull import get_job_summary_from_url
from base_resume_extractor import json_extractor
from prompt_generator import create_llm_prompt
from json_reconstruction import get_raw_multiline_input, create_new_resume


# Step 1 -> Prompt the user for the job URL and extract the job description summary
webpage_url = input("\nNote - Do Not give a URL with multiple job profiles, make sure the weblink holds only 1 job posting.\nEnter the URL of the job description: ")
job_summary = get_job_summary_from_url(webpage_url)

# Step 2 -> Load JSON File
base_resume_path = 'data/base_resume.json'
base_resume = json_extractor(base_resume_path)

# Step 4 -> Define the Flags. These flags tell the LLM which parts of the resume can be altered to better fit
# the new resume.
flags = {
    'summary': True,
    'headline': True,
    'work': True,
    'education': True,
    'skills': True,
    'certifications': True,
    'awards': True,
    'publications': True,
    'languages': True,
    'interests': True,
    'volunteer': True,
    'projects': True,
    'references': True
}

#Step 5 -> Generate Prompt
prompt = create_llm_prompt(job_summary,base_resume,flags)

#Step 6 -> Copy the prompt to clipboard
pyperclip.copy(prompt)
print("\nPrompt Copied to your Clipboard. \nKindly use the prompt on a LLM and copy the response.")

#Step 7 -> Take the Input from the LLM and sanitize it
new_resume_path = 'data/updated_resume.json'
raw_json = get_raw_multiline_input()
create_new_resume(base_resume_path, raw_json, new_resume_path)
print("\n Updated Resume Created for rxresu.me. Upload the JSON as Import it as a Reactive Resume JSON and Enjoy.")
