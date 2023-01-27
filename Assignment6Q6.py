def student_data(student_id, **kwargs):
    print(f'\nStudent ID: {student_id}')
    if 'student_name' and 'student_class' in kwargs:
        print(f"Student Name:  {kwargs['student_name']}")
        print(f"Student Class:  {kwargs['student_class']}")
    elif 'student_name' in kwargs:
        print(f"Student Name:  {kwargs['student_name']}")

student_data(student_id='22103028', student_name='Gaurav Gupta')

student_data(student_id='22103028', student_name='Gaurav Gupta', student_class='CSE-G1')