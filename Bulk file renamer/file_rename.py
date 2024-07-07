import os

def main():
    i = 0
    path = "" # directory name
    for filename in os.listdir(path):
        my_file = "testname" + str(i) + ".txt"
        my_src = path + filename
        my_file = path + my_file
        os.rename(my_src, my_file)
        i+=1

if __name__ == '__main__':
    main()





# with open('data.txt' , 'w') as f:
#     data = 'The web involves the internet'
#     f.write(data)

# try:
#     with open("file.log") as file:
#         read_data = file.read()
# except:
#     print("Couldn't open file.log")