import json


def get_candidates():
    with open('candidates.json', 'r', encoding='utf-8') as file:
        candidates = json.loads(file.read())
    return candidates


def search_skill(skill):
    result = '<pre>'
    for candidate in get_candidates():
        skills = candidate['skills'].lower()
        skills = skills.split(', ')
        if skill.lower() in skills:
            result += (
                f"{candidate['name']}\n"
                f"{candidate['position']}\n"
                f"{candidate['skills']}\n\n"
            )
    result += '</pre>'
    return result


def candidate_page(candidate_id):
    candidates = get_candidates()
    for candidate in candidates:
        if candidate['id'] == candidate_id:
            candidate_id -= 1
            result = '<pre>\n'
            result += (
                f"""<img src="{candidates[candidate_id]['picture']}"/>\n\n"""
                f"{candidates[candidate_id]['name']}\n"
                f"{candidates[candidate_id]['position']}\n"
                f"{candidates[candidate_id]['skills']}\n\n"
            )
            result += '</pre>'
            return result
        else:
            continue
    return 'Нет кандидата с таким ID.'
