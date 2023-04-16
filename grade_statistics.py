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
    threshold = [14, 17, 20, 23, 27, 30]
    for i in range(6):
        if points <= threshold[i]:
            return i


def get_total_points(results: list):
    return [exam + int(exercise * 0.1) for exam, exercise in results]


def get_final_grades(results: list):
    final_grades = []
    for exam, exercise in results:
        final_grades.append(0) if exam < 10 \
            else final_grades.append(get_grade(exam + int(exercise * 0.1)))
    return final_grades


def print_statistics(points: list):
    print("Statistics:")
    print("Points average:", sum(get_total_points(points)) / len(points))
    pp = (len(points) - get_final_grades(points).count(0)) * 100 / len(points)
    print(f"Pass percentage: {pp:.1f}")
    print("Grade distribution:")
    for n in range(5, -1, -1):
        print(f"{n}:", '*' * get_final_grades(points).count(n))


print_statistics(get_results())
