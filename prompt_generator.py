

def create_llm_prompt(job_desc_summary, resume_data, flags):
    prompt = '''DO EXACTLY AS I SAY.
    I will be giving you a Job Description and a base resume in JSON format.
    You are going to create an updated resume which is based on the base resume that is better fit for the job description.
    Your reply should be in the EXACT same FORMAT as the base resume however you can change the text based on the flags. 
    You are NOT allowed to alter the schema or format of the JSON.
    Based on the flags, if a flag is true you are allowed to alter the text in that section or subsection (flags are named like 'section' or 'section_subsection') to make it more fit and ATS friendly based on the job description
    In Work Experience, Do NOT Change the firm or company. 
    Write ONLY in MarkDown. 
    Always be specific in your answers and do not leave anything for the user to add. Add REALISTIC dates, degrees, institutions, and other fields if needed. DO NOT add "Instituion Name" or "XYZ University" anything you wouldnt see in a resume.
    Make sure when updating the text, that you keep the length of the new text almost as much old one. 
    Finally, make logical additions only. For example, one cannot have a PhD without Masters and thus the additions or edits need to be valid as well. 
    Give Emphasis to requirements. Make sure the keywords ats systems look for are present in the updated dataset 
    
    Job Description:
    {}
    
    JSON base resume:
    {}
    
    Flags :
    {}
    
    Respond only in code block. Response: 
    '''.format(job_desc_summary, resume_data, flags)
    return prompt
