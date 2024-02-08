from S1E7 import Baratheon, Lannister


def main():
    try:
        Robert = Baratheon("Robert")
        print(Robert.__dict__)
        print(Robert.__str__)
        print(Robert.__repr__)
        print(Robert.is_alive)
        Robert.die()
        print(Robert.is_alive)
        print(Robert.__doc__)
        print("---")
        Cersei = Lannister("Cersei")
        print(Cersei.__dict__)
        print(Cersei.__str__)
        print(Cersei.is_alive)
        print("---")
        Jaine = Lannister.create_lannister("Jaine", True)
        print(
            f"Name: {Jaine.first_name, type(Jaine).__name__}, "
            f"Alive: {Jaine.is_alive}"
        )

    except Exception as e:
        print(type(e).__name__ + ":", e)
        exit(1)


if __name__ == "__main__":
    main()
