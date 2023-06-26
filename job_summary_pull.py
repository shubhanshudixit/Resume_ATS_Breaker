import re
from newspaper import Article

# Initialize variables
webpage_url = ""
job_desc_main_content = ""
job_desc_summary = ""

# Function to extract the main content from a webpage URL
def extract_main_content(url):
    article = Article(url)
    article.download()
    article.parse()
    main_content = article.text.strip()
    main_content = re.sub(r'\n\s*\n', '\n\n', main_content)
    return main_content

# Function to format the content into sections
def format_content(content):
    sections = re.split(r'\n\s*\n', content)
    sections = [section.strip() for section in sections]
    formatted_content = '\n\n'.join(sections)
    return formatted_content

def get_job_summary_from_url(url):
    job_desc_main_content = extract_main_content(url)
    job_desc_summary = format_content(job_desc_main_content)
    return(job_desc_summary)