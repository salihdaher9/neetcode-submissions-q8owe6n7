class MinStack:

    def __init__(self):
        self.stack=[]
        self.minn=[]
        

    def push(self, val: int) -> None:
        if not self.stack and not self.minn:
            self.minn.append(val)
            self.stack.append(val)
            return

        self.stack.append(val)
        if self.minn[-1]>val:
            self.minn.append(val)
        else:
            self.minn.append(self.minn[-1])

    def pop(self) -> None:
        self.stack.pop()
        self.minn.pop()


    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minn[-1]
