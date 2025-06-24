# try:
#     fhandler = open('test.txt', 'w')
#     fhandler.write('Hello World')
# except IOError as ex:
#     print("Error performing I/O operations on the file: ",ex)
# finally:
#     if fhandler:
#         fhandler.close()

wor = ["Hello world","It's the first exercise in I/O","That mean it is number 1","Not 2","Not three","It is exciting","And i am all 4 it&quot"]
try:
    with open('my_test.txt', 'w') as fhandler:
        for r in wor:
            fhandler.write(r + '\n')
except IOError as ex:
    print("Error performing I/O operations on the file: ",ex)

try:
    with open('my_test.txt','r') as f:
        line = f.readline()
        while (line != ''):
            for l in line:
                if l.isnumeric():
                    print(line, end="")
                    break
            line = f.readline()
except IOError as ex:
    print("Error " + ex)



try:
    with open("my_test.txt",'r') as file:
        lines = file.readlines()
        for l in lines:
            if len(l.split(' ')) %2 == 0:
                print(l.rstrip())

        for l in lines:
            count = 0
            for w in l.split(" "):
                if not w.strip().isnumeric():
                    count += 1
            print(count)

        for l in lines:
            print(sum(len(x.strip()) for x in l.split()))

        # סעיף 5
except:
    print()



try:
    with open("summary.txt.",'w') as newF , open("my_test.txt","r") as oldF:
        for l in oldF:
            newF.write( f"{l.rstrip()} ({len(l.split())})")

except:
    print()