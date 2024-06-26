marks_per_subject = {
    "science": 100,
    "english": 80,
    "math": 80
}

total_marks = sum(marks_per_subject.values())

get_mark_science = int(input("Please enter your marks in science: "))
get_mark_english = int(input("Please enter your marks in english: "))
get_mark_math = int(input("Please enter your marks in math: "))



get_total_marks = sum((get_mark_math, get_mark_english, get_mark_science))

is_pass_parcentage = get_mark_english >= marks_per_subject["english"] * 0.4 and get_mark_science >= marks_per_subject["science"] * 0.4 and get_mark_math >= marks_per_subject["math"] * 0.4

if (get_total_marks >= (total_marks / 100) * 40 and is_pass_parcentage) :
    print("You pass the exam good luck", get_total_marks)
else :
    print("You failed to pass the exam, try again next year", get_total_marks)
