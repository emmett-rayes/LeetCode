class MyQueue:
    def __init__(self):
        self.back = []
        self.front = []

    def push(self, x: int) -> None:
        self.back.append(x)

    def pop(self) -> int:
        self.balance()
        return self.front.pop()

    def peek(self) -> int:
        self.balance()
        return self.front[-1]

    def empty(self) -> bool:
        return len(self.front) + len(self.back) == 0

    def balance(self):
        if len(self.front) == 0:
            while len(self.back) != 0:
                self.front.append(self.back.pop())
