
def get_grade():
    """
    get grade from user input and print the number of valid grades, the average and the highest grade
    :return: None
    """
    valid_grade = []
    while True:
        try:
            grade = int(input('Enter grade: '))
            if grade == -999:
                if len(valid_grade) < 10:
                    print('Need at least 10 valid grades, keep entering')
                    continue
                break
            if grade < 0 or grade > 100:
                raise Exception('Not in range')
            valid_grade.append(grade)


        except ValueError:
            print('Invalid input,skip')
        except Exception:
            print('Not in range,skip')

    print(f"Number of valid grades {len(valid_grade)}")
    print(f"Class average {sum(valid_grade)/len(valid_grade)}")
    print(f"Highest grade {max(valid_grade)}")

get_grade()
