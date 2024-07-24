#Assignment-3 #Question-1

class TC_Stack:
    def __init__(self, capacity):
        # Initialize the two-color double-stack with a given capacity
        self.capacity = capacity
        # Create an array to store elements of both stacks (red & blue)
        self.stack_array = [None] * capacity
        # Initialize the top pointer for the red stack to -1 (empty)
        self.Top = -1
        # Initialize the top pointer for the blue stack to the capacity (empty)
        self.blueTop = capacity

    def is_red_stack_empty(self):
        # Check if the red stack is empty (top pointer is at -1)
        return self.Top == -1

    def is_blue_stack_empty(self):
        # Check if the blue stack is empty (top pointer is at the capacity)
        return self.blueTop == self.capacity

    def is_full(self):
        # Check if the double-stack is full (red top + 1 is equal to blue top)
        return self.Top + 1 == self.blueTop

    def red_push(self, value):
        # Push an element onto the red stack
        if self.Top + 1 == self.blueTop:
            raise Exception("Red stack is full")  # Check if the red stack is already full
        self.Top += 1  # Move the red top pointer up
        self.stack_array[self.Top] = value  # Store the value in the red stack

    def blue_push(self, value):
        # Push an element onto the blue stack
        if self.Top + 1 == self.blueTop:
            raise Exception("Blue stack is full")  # Check if the blue stack is already full
        self.blueTop -= 1  # Move the blue top pointer down
        self.stack_array[self.blueTop] = value  # Store the value in the blue stack

    def red_pop(self):
        # Pop an element from the red stack
        if self.is_red_stack_empty():
            raise Exception("Red stack is empty")  # Check if the red stack is already empty
        value = self.stack_array[self.Top]  # Get the value from the top of the red stack
        self.Top -= 1  # Move the red top pointer down
        return value

    def blue_pop(self):
        # Pop an element from the blue stack
        if self.is_blue_stack_empty():
            raise Exception("Blue stack is empty")  # Check if the blue stack is already empty
        value = self.stack_array[self.blueTop]  # Get the value from the top of the blue stack
        self.blueTop += 1  # Move the blue top pointer up
        return value

    def red_top_element(self):
        # Get the top element of the red stack
        if self.is_red_stack_empty():
            raise Exception("Red stack is empty")  # Check if the red stack is empty
        return self.stack_array[self.Top]  # Return the value at the top of the red stack

    def blue_top_element(self):
        # Get the top element of the blue stack
        if self.is_blue_stack_empty():
            raise Exception("Blue stack is empty")  # Check if the blue stack is empty
        return self.stack_array[self.blueTop]  # Return the value at the top of the blue stack




def main():
    # Create a two-color double-stack object with a capacity of 10
    tc_stack = TC_Stack(10)

    # Push elements onto the red stack
    tc_stack.red_push(1)
    tc_stack.red_push(2)
    tc_stack.red_push(3)

    # Push elements onto the blue stack
    tc_stack.blue_push(11)
    tc_stack.blue_push(12)
        
    # Print the top elements of both stacks
    print("Red top element:", tc_stack.red_top_element())
    print("Blue top element:", tc_stack.blue_top_element())  

    # Pop elements from both stacks
    tc_stack.red_pop()
    tc_stack.blue_pop()

    # Print the top elements of both stacks after the pop operations
    print("Red top element after poping:", tc_stack.red_top_element()) 
    print("Blue top element after poping:", tc_stack.blue_top_element()) 

if __name__ == "__main__":
    main()
