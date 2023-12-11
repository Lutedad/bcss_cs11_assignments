############################################
f = open("file1.txt","r")
k = 0
count = 0
execute = False
msg = ""
#-------------------------------------------
raw = f.readlines()
new_list = []
for item in raw:
    new_list.append(item.strip().split())
#-------------------------------------------
for i in range(len(new_list)):
    for j in range(len(new_list[i])):
        new_list[i][j] = int(new_list[i][j]) * 2
        msg += f"{new_list[i][j]} "
    msg += "\n"
f.close()
############################################
f_w = open("file1_result.txt","w")
f_w.write(msg)
f_w.close()
############################################
f_r = open("file1_result.txt","r")
print(f_r.read())
f_r.close()
#################Future research -> Is there any possible ways to read & write at the same time?