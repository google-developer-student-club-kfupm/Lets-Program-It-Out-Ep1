"""
Algorithm (The Best Team)
"""

import itertools
import json

GRADES = [4.00, 3.75, 3.50, 3.00, 2.50, 2.00]


def calculate_gpa(earned_hours, current_gpa, next_term_grades, next_term_credits):
    points = earned_hours * current_gpa

    next_term_points = 0
    for i in range(len(next_term_grades)):
        next_term_points += next_term_grades[i] * next_term_credits[i]

    total_points = points + next_term_points
    return total_points / (earned_hours + sum(next_term_credits))


def get_possibilties(credits, earned_hours, current_gpa):
    possible_grades = [p for p in itertools.product(
        GRADES, repeat=len(credits))]

    term_possibilites = []
    for grade_possibility in possible_grades:
        term_gpa = calculate_gpa(earned_hours, current_gpa,
                                 grade_possibility, credits)
        credit_grades_dicts = []
        for i in range(len(grade_possibility)):
            credit_grades_dicts.append(
                {"credit": credits[i], "grade": grade_possibility[i]})

        reponse = {
            "term": credit_grades_dicts,
            "gpa": term_gpa
        }
        term_possibilites.append(reponse)
    return term_possibilites


def main():
    credits = [4, 3, 2, 3]
    earned_hours = 20
    current_gpa = 3.150

    list = get_possibilties(credits, earned_hours, current_gpa)

    file = open("text.txt", "w")
    file.write(json.dumps(list, indent=4, sort_keys=True))
    file.close()


main()
