class MyQueue:

    def __init__(self):
        self.st=[]
        self.stt=[]
        

    def push(self, x: int) -> None:
        self.st.append(x)
        

    def pop(self) -> int:
        if len(self.stt)==0:
            while self.st :
                self.stt.append(self.st[-1])
                self.st.pop()
        val=self.stt[-1]
        self.stt.pop() 
        return val        

    def peek(self) -> int:
        if len(self.stt)==0:
            while self.st :
                self.stt.append(self.st[-1])
                self.st.pop()
        return self.stt[-1]    


        

    def empty(self) -> bool:
        return len(self.st)==0 and len(self.stt)==0

        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()