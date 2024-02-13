from new_student import Student


def main():
    try:
        student = Student(name="Edward", surname="agle")
        print(student)
    except Exception as e:
        print(type(e).__name__ + ":", e)
    print("----------------------------")
    try:
        student = Student(name="Edward", surname="agle", id="toto")
        print(student)
    except Exception as e:
        print(type(e).__name__ + ":", e)
    print("----------------------------")
    try:
        student = Student(name="Edward", surname="agle", login="toto")
        print(student)
    except Exception as e:
        print(type(e).__name__ + ":", e)
    print("----------------------------")
    try:
        student = Student(name="Bernard", surname="agel", active=False)
        print(student)
    except Exception as e:
        print(type(e).__name__ + ":", e)
    print("----------------------------")


if __name__ == "__main__":
    main()
