import json


def get_raw_multiline_input():
    print("\nEnter the JSON input (press Enter three times to finish input):")
    lines = []
    empty_lines_count = 0

    while empty_lines_count < 3:
        line = input()
        if line:
            lines.append(line)
            empty_lines_count = 0
        else:
            empty_lines_count += 1

    input_json = '\n'.join(lines)

    try:
        # Load the JSON string into a JSON object
        data = json.loads(input_json)

        # Convert the JSON object into a single-line string
        single_line_string = json.dumps(data, separators=(",", ":"))

        print("Single-line string representation:")
        print(single_line_string)
        return single_line_string
    except json.JSONDecodeError as e:
        print("Error: Invalid JSON input.")
        print(e)

def create_new_resume(base_resume_path, updated_extract, new_resume_path):
    # Open Base Resume File
    with open(base_resume_path) as json_file:
        json1_data = json.load(json_file)
    # Get updated JSON Extract
    json2_data = json.loads(updated_extract)
    # Create a New JSON
    new_json_data = json1_data

    if 'summary' in json2_data:
        new_json_data['basics']['summary'] = json2_data['summary']

    if 'headline' in json2_data:
        new_json_data['basics']['headline'] = json2_data['headline']

    if 'work' in json2_data and len(json2_data['work']) > 0:
        new_json_data['sections']['work']['items'] = json2_data['work']

    if 'education' in json2_data and len(json2_data['education']) > 0:
        new_json_data['sections']['education']['items'] = json2_data['education']

    if 'skills' in json2_data and len(json2_data['skills']) > 0:
        new_json_data['sections']['skills']['items'] = json2_data['skills']

    if 'projects' in json2_data and len(json2_data['projects']) > 0:
        new_json_data['sections']['projects']['items'] = json2_data['projects']

    if 'interests' in json2_data and len(json2_data['interests']) > 0:
        new_json_data['sections']['interests']['items'] = json2_data['interests']

    if 'languages' in json2_data and len(json2_data['languages']) > 0:
        new_json_data['sections']['languages']['items'] = json2_data['languages']

    if 'volunteer' in json2_data and len(json2_data['volunteer']) > 0:
        new_json_data['sections']['volunteer']['items'] = json2_data['volunteer']

    if 'references' in json2_data and len(json2_data['references']) > 0:
        new_json_data['sections']['references']['items'] = json2_data['references']

    if 'publications' in json2_data and len(json2_data['publications']) > 0:
        new_json_data['sections']['publications']['items'] = json2_data['publications']

    if 'certifications' in json2_data and len(json2_data['certifications']) > 0:
        new_json_data['sections']['certifications']['items'] = json2_data['certifications']

    # Save the new JSON
    with open(new_resume_path, 'w') as json_file:
        json.dump(new_json_data, json_file, indent=4)
