# Resume_ATS_Breaker
Just a bunch of scripts that help you quickly create ATS-friendly resumes using AI chat prompts. 
Currently txt_interface is the main script to interact with the application.
Steps - 
1. Take a resume JSON [/data/base_resume.json] (created via reactive resume - rxresu.me, which is an open source application for building apps)
2. Ask the user for the job link URL
3. Creates a prompt for ChatGPT and copies it to the user's clipboard
4. The user places the prompt into ChatGPT or Bing
5. The user copies the code block reponse from the Chat-based LLM
6. The user is prompoted to paste the new code block back in the application
7. The application then generates a new JSON which can be imported into Reactive Resume
8. And, Voilà! you have resume thats based on your base resume but is ATS friendly with respect to the specific job descrption.

Future Scope - 
1. Directi Connection to OpenAI's API - Neeeds $$$
2. Script to automatically find jobs based on thresholds
3. Automate the process further using Selenium or browser extension
4. Automation of the Job Application Process
