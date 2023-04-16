def get_results():
    results = []
    while True:
        user_input = input("Exam points and exercises completed: ")
        if user_input == "":
            break
        results.append((int(user_input.split(" ")[0]),
                        int(user_input.split(" ")[1])))
    return results


def get_grade(points):
    if points <= 14:
        return 0
    if points <= 17:
        return 1
    if points <= 20:
        return 2
    if points <= 23:
        return 3
    if points <= 27:
        return 4
    if points <= 30:
        return 5


def get_total_points(results: list):
    return [exam + int(exercise * 0.1) for exam, exercise in results]


def get_final_grades(results: list):
    final_grades = []
    for exam, exercise in results:
        if exam < 10:
            final_grades.append(0)
        else:
            final_grades.append(get_grade(exam + int(exercise * 0.1)))
    return final_grades


def print_statistics(points: list):
    print("Statistics:")
    print("Points average:", sum(get_total_points(points)) / len(points))
    pp = (len(points) - get_final_grades(points).count(0)) * 100 / len(points)
    print(f"Pass percentage: {pp:.1f}")
    print(f"""Grade distribution:
  5: {"*" * get_final_grades(points).count(5)}
  4: {"*" * get_final_grades(points).count(4)}
  3: {"*" * get_final_grades(points).count(3)}
  2: {"*" * get_final_grades(points).count(2)}
  1: {"*" * get_final_grades(points).count(1)}
  0: {"*" * get_final_grades(points).count(0)}""")

print_statistics(get_results())
