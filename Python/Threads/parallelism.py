from multiprocessing import Process

# Parralelism is executing multiple tasks at the same time. Multiple processors are assigned processes to execute them parallely.


def calculate_percentage (total_marks, obtained_marks):
    """
    Function to calculate the percentage of a student.
    Params: 
        Total marks: The total marks of the examination
        Obtained marks: Marks obtained by the student
    Returns:
        The total percentage obtained by the student
    """

    percentage_obtained = obtained_marks/ total_marks
    return percentage_obtained


def calculate_obtained_marks (maths_marks, sci_marks, social_marks, eng_marks, hind_marks):
    """
    Function to calculate the total marks obtained by a student.
    Params:
        math_marks: Marks obtained in maths
        sci_marks: Marks obtained in science
        social_marks: Marks obtained in social
        eng_marks: Marks obtained in english
        hind_marks: Marks obtained in hindi
    Returns: 
        The total marks obtained by the student
    """

    obtained_marks = maths_marks + sci_marks + social_marks + eng_marks + hind_marks
    return obtained_marks


if __name__ == "__main__":
    students = [
        Process(target=calculate_obtained_marks, args=(89, 91, 83, 80, 90))
        for i in range(5)
    ]
    
    # only created not started, so no process id
    for student in students:
        print(student)

    # started the processes
    for student in students:
        student.start()

    print("----------------------------------")

    # it is started, thus has a pid
    for student in students:
        print(student)

    # it is completed, hence stopped
    for student in students:
        student.join()

    print("----------------------------------")

    for student in students:
        print(student)

    print("----------------------------------")
    
    
    
