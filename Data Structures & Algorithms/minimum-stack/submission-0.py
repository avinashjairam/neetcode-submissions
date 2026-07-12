class MinStack:

    def __init__(self):
        # 'min' keeps track of the current minimum value in the stack
        self.min = float('inf')
        # 'stack' stores differences between pushed values and the current min
        self.stack = []

    def push(self, val: int) -> None:
        # if the stack is empty, this is the first element
        if not self.stack:
            # store 0 since val-val = 0 (difference is zero)
            self.stack.append(0)
            # initialize 'min' to this first value 
            self.min = val
        else:
            # store the difference between current val and current min
            diff = val - self.min
            self.stack.append(diff)

            # if val is smaller than current min, update min
            # a negative diff means the new value is the new minimum 
            if val < self.min:
                self.min = val


    def pop(self) -> None:
        # if stack is empty, do nothing
        if not self.stack:
            return 

        # pop the top difference value 
        pop = self.stack.pop()

        # if the popped difference is negative, it means the popped value was the 
        # current min and we need to restore the previous min 
        if pop < 0:
            # restore the previous min using the relation:
            # new_min = current_min - pop_difference 
            # (since pop_differnce = val-old_min and val == current_min)
            self.min = self.min-pop

    def top(self) -> int:
        # get the top difference
        top = self.stack[-1]

        # if top > 0, it means val > current_min, so we reconstruct the original value
        if top > 0:
            return top + self.min
        else:
            # if top <=0, it means the top value is the current minimum
            return self.min

        

    def getMin(self) -> int:
        # simply return the current minimum
        return self.min
        
