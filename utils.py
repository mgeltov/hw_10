import json
from classes import Candidate

def load_candidates(json_file):

    with open(json_file, 'r', encoding="utf-8") as file:
        data = json.load(file)

    candidates = []
    for element in data:
        pk = element["pk"]
        name = element["name"]
        picture = element["picture"]
        position = element["position"]
        gender = element["gender"]
        age = element["age"]
        skills = element["skills"]
        candidate = Candidate(pk, name, picture, position, gender, age, skills)
        candidates.append(candidate)

    return candidates


def get_all(json_file):
    candidates = load_candidates(json_file)
    candidates_list = []
    for candidate in candidates:
        candidates_list.append(candidate.get_all())
    return candidates_list


def get_by_pk(json_file, pk):
    candidates = load_candidates(json_file)
    for candidate in candidates:
        if pk == candidate.get_pk():
            return candidate.get_by_pk(pk)


def get_by_skills(json_file, skill):
    candidates = load_candidates(json_file)
    candidates_list = []
    for candidate in candidates:
        candidates_skills_list = str.lower(candidate.get_skills()).split(', ')
        if str.lower(skill) in candidates_skills_list:
            candidates_list.append(candidate.get_all())
    return candidates_list


def get_by_name(json_file, name):
    candidates = load_candidates(json_file)
    candidates_list = []
    for candidate in candidates:
        if str.lower(name) in str.lower(candidate.name):
            candidates_list.append(candidate.get_all())
    return candidates_list