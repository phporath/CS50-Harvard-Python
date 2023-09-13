class Jar:
    def __init__(self, capacity=12):
        if isinstance(capacity, int) and capacity > 0:
            self._capacity = capacity
            self._present = 0
        else:
            raise ValueError("is not a non-negative int.")

    def __str__(self):
        cokie = "🍪"
        return f"{self._present * cokie}"

    def deposit(self, n=None):
        if self._present + n > self._capacity:
            raise ValueError("Exceeds jar capacity")
        self._present = self._present + n

    def withdraw(self, n=None):
        if self._present < n:
            raise ValueError("Not enough cokie in the jar")
        self._present = self._present - n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._present


def main():
    jar = Jar(5)
    print(f"Initial amount of cockie: {str(jar)}")
    jar.deposit(3)
    print(f"Jar after deposit: {str(jar)}")
    jar.withdraw(2)
    print(f"Jar after withdrawal: {str(jar)}")
    print(f"Jar capacity: {jar.capacity}")
    print(f"Jar size: {jar.size}")


if __name__ == "__main__":
    main()
