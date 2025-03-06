# for i in range(1, 5, 2):
#    print(i)

my_string = "Hello there, I have to visit more places in Gdynia!!!"
new_string = my_string * 200
# print(new_string)

counter = 0

for i in new_string:
    if i == 'a':
        #print("I've found the a letter!!!")
        counter = counter + 1

print("The number of found letters: ", counter)
