from DiamondTrap import King


def main():
    try:
        Joffrey = King("Joffrey")
        print(Joffrey.__dict__)
        Joffrey.set_eyes("blue")
        Joffrey.set_hairs("light")
        print(Joffrey.get_eyes())
        print(Joffrey.get_hairs())
        print(Joffrey.__dict__)
        # addtional tests
        print("-----------------------")
        print(Joffrey.__class__.__mro__)
        print(Joffrey.__class__.__bases__)
        Joffrey.printHello()
        print("-----------------------")
    except Exception as e:
        print(type(e).__name__ + ":", e)


if __name__ == "__main__":
    main()
