from S1E9 import Stark
# from S1E9 import Character


def main():
    """
    Test function for the Stark class.
    """
    try:
        # hodor = Character("hodor") # should raise an error
        Ned = Stark("Ned")
        print(Ned.__dict__)
        print(Ned.is_alive)
        Ned.die()
        Ned.sing()
        print(Ned.is_alive)
        print(Ned.__doc__)
        print(Ned.__init__.__doc__)
        print(Ned.die.__doc__)
        print("---")
        Lyanna = Stark("Lyanna", False)
        print(Lyanna.__dict__)

    except Exception as e:
        print(type(e).__name__ + ":", e)
        exit(1)


if __name__ == "__main__":
    main()
