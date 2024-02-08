

class calculator:
    """
    This class is a simple calculator that can perform
    calculations (dot product, addition, sub-traction)
    of 2 vectors.
    """

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """Calculate the dot product of two vectors."""
        sum = 0
        for i in range(len(V1)):
            sum = sum + V1[i] * V2[i]
        print(sum)

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """Add two vectors."""
        sum = [float(V1[i] + V2[i]) for i in range(len(V1))]
        print(sum)

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """Subtract two vectors."""
        sub = [float(V1[i] - V2[i]) for i in range(len(V1))]
        print(sub)
