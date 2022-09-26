from ast import Break
 
frame = []
index = []
 
process_list = []
 
n = int(input("Enter the number of string elements you want: "))
 
for i in range(n):
    ele = int(input("Enter the String element: "))
    process_list.append(ele)
 
print(process_list)
 
f_no = int(input("Enter the frame number: "))
 
for i in process_list:
 
    if(len(frame) == f_no):
        for j in frame:
            if i == j:
                print("HIT!!")
                print(frame)
                Break
    
        else:
            print("MISS!!")
            index.append(i)
            replace = frame.index(j)
            frame.insert(replace,i)
            frame.remove(j)
            print(frame)
 
    else:
        frame.append(i)
        print("MISS!!")
        index.append(i)
        print(frame)
