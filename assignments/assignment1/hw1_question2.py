"""
__author__ = Hagai Har-Gil
HW1 Question 2 Solution
"""


def compare_subjects_within_student(subj1_all_students, subj2_all_students):
    """Compare the two subjects with their students and print out the "preferred"
    subject for each student.

    Single-subject students shouldn't be printed.

    Parameters
    ----------
    subj1_all_students, subj2_all_students : dict
        Dictionary with student names as keys, and their grades as a tuple.
        It should also contain a mandatory "subject" key which contains the
        subject's name.

    Returns
    -------
    result_table : dict
        Dictionary with subject names as keys, and students which were found
        to have better grades in it as the list of values.
    """
    subj1 = subj1_all_students.pop("subject")
    subj2 = subj2_all_students.pop("subject")

    # I keep the output in a dictionary of lists, one 'column' for each subject
    result_table = {subj1: [], subj2: []}

    for key, val in subj1_all_students.items():
        if key in subj2_all_students:
            if max(val) >= max(subj2_all_students[key]):
                result_table[subj1].append(key)
            else:
                result_table[subj2].append(key)
    print(result_table)
    return result_table


if __name__ == "__main__":
    print("Question 2 solution:")
    subj1 = {
        "Jack": (75, 95),
        "Jenny": (80, 90),
        "Matt": (66, 77),
        "Dana": (100, 90),
        "Rob": (70, 70),
        "subject": "History",
    }
    subj2 = {
        "Jack": (45, 85),
        "Jenny": (80, 91),
        "Matt": (66, 77),
        "Georgia": (83, 91),
        "Rob": (62, 70),
        "subject": "Chemistry",
    }
    compare_subjects_within_student(subj1, subj2)
    # Notice how Dana and Georgia are missing
