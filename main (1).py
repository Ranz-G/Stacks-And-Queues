class Stack:
        def __init__(self):
            self.stack = []

        def push(self, item):

            self.stack.append(item)

        def pop(self):
            if not self.is_empty():
                return self.stack.pop()
            return "Stack is empty"

        def peek(self):
            if not self.is_empty():
                return self.stack[-1]
            return "Stack is empty"

        def is_empty(self):
            return len(self.stack) == 0


class Queue:
        def __init__(self):

            self.queue = []

        def enqueue(self, item):

            self.queue.append(item)

        def dequeue(self):
            if not self.is_empty():
                return self.queue.pop(0)
            return "Queue is empty"

        def front(self):
            if not self.is_empty():
                return self.queue[0]
            return "Queue is empty"

        def is_empty(self):
            return len(self.queue) == 0

class StackQueueProject:
        def __init__(self):
            self.stack = Stack()
            self.queue = Queue()

        def reverse_list(self, lst):
            print("Reversing the list using stack:")
            for item in lst:
                self.stack.push(item)
                print(f"Pushed {item} onto stack:")

            reversed_lst = []
            while not self.stack.is_empty():
                popped_item = self.stack.pop()
                reversed_lst.append(popped_item)
                print(f"Popped {popped_item} from stack.")

            return reversed_lst

        def process_tasks(self, tasks):
            print("Processing tasks using queue:")
            for task in tasks:
                self.queue.enqueue(task) 
                print(f"Enqueued task: {task}")

            processed_tasks = []
            while not self.queue.is_empty():
                dequeued_task = self.queue.dequeue()
                processed_tasks.append(dequeued_task) 
                print(f"Dequeued and processed task: {dequeued_task}")

            return processed_tasks


class inputs():

        def longinput(list):

            sample_list = [var.strip() for var in list.split(",")]
            return sample_list

        def sorted_longinput(list):
            sample_list = [var.strip() for var in list.split(",")]
            sorted_sample_list = sorted(sample_list)
            return  sorted_sample_list
        def tasklist(list):
            
            sample_tasks = [var.strip() for var in long_task_input.split(",")]
            orig_task_list = []
            for i, vars in enumerate(sample_tasks):
                temp = [var.strip() for var in vars.split(" ")]
                orig_task_list.append(temp)
            sorted_task_list = sorted(orig_task_list)
            print(f"Original Task list: {orig_task_list}") 
    
            print(f"Sorted Task list: {sorted_task_list}") 
            temp_cont = []
            o = 0
            for task in sorted_task_list:
                text = str(sorted_task_list[o][1])
                temp_cont.append(text)
                o+=1
            return temp_cont
if __name__ == "__main__":
        project = StackQueueProject()
        long_input = input("Enter numbers seperated by commas in any order (example 1,2,3,7,6): ")

        print("Original List:", inputs.longinput(long_input))
        print("Sorted List:", inputs.sorted_longinput(long_input))


        reversed_list = project.reverse_list(inputs.sorted_longinput(long_input))
        print("Reversed List:", reversed_list)


        print("Add number and a space at the beginning of every task")
        print("Example: 1 Wakeup, 2 Breakfast, 3 Exercise, ... etc")
        long_task_input = input("Enter tasks here: ")    
value = inputs.tasklist(long_task_input)
print("\nTasks to process:", value)
processed_tasks = project.process_tasks(value)
print("Processed tasks:", processed_tasks)