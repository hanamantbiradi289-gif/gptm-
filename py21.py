class priorityQueueEntry:
    def __init__(self,value,p):
        self.value=value
        self.p=p
class priorityQueue:
    def __init__(self):
        self.qlist=[]
    def IsEmpty(self):
        return len(self.qlist)==0
    def queue_Length(self):
        return len (self.qlist)
    def Enqueue(self,value,priority):
        data_item=priorityQueueEntry(value,priority)
        self.qlist.append(data_item)
    def Dequeue(self):
        if self.IsEmpty():
            print("cannot perform dequeue operation")
            return
        else:
            highest_priority=self.qlist[0].p
            index=0
            for i in range(0,self.queue_Length()):
                if highest_priority>self.qlist[i].p:
                    highest_priority=self.qlist[i].p
                    indwx=i
            del_item=self.qlist.pop(index)
            print("the deleted item is ",del_item.value)
    def display(self):
        if self.IsEmpty():
            print("Queue is empty")
        else:
            for x in range(0,self.queue_Length()):
                print(self.qlist[x].value,":",self.qlist[x].p)
pq=priorityQueue()
while (True):
    print("1:enqueue 2:dequeue 3:display 4:Length 5:exit")
    choice=int(input("Enter your choice:"))
    if choice==1:
        value=input("enter the item to insert:")
        priority=int(input("Enter the priority:"))
        pq.Enqueue(value,priority)
    elif choice==2:
        pq.Dequeue()
    elif choice==3:
        pq.display()
    elif choice==4:
        print("length of queue is:",pq.queue_Length())
    else:
       break
    
            
