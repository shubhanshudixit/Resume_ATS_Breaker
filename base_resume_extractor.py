import json

def json_extractor(path_to_json):

    # Read the base resume JSON file and extract the essential sections
    with open(path_to_json) as json_file:
        data = json.load(json_file)

    essential_sections = [
        'summary',
        'headline',
        'work',
        'education',
        'skills',
        'certifications',
        'awards',
        'publications',
        'languages',
        'interests',
        'volunteer',
        'projects',
        'references'
    ]

    extracted_data = {}

    for section in essential_sections:
        if section == 'summary' or section == 'headline':
            extracted_data[section] = data['basics'][section]
        elif section in data['sections']:
            items = []
            for item in data['sections'][section]['items']:
                item_data = {}
                if 'name' in item:
                    item_data['name'] = item['name']
                if 'summary' in item:
                    item_data['summary'] = item['summary']
                if 'position' in item:
                    item_data['position'] = item['position']
                if 'area' in item:
                    item_data['area'] = item['area']
                if 'date' in item:
                    item_data['date'] = item['date']
                if 'end' in item:
                    item_data['end'] = item['end']
                if 'start' in item:
                    item_data['start'] = item['start']
                if 'degree' in item:
                    item_data['degree'] = item['degree']
                if 'institution' in item:
                    item_data['institution'] = item['institution']
                if item_data:
                    items.append(item_data)
            if items:
                extracted_data[section] = items

    resume_data = json.dumps(extracted_data, indent=1)
    return(resume_data)