# _*_ coding: utf-8 _*_
import time as TIME
import os
start_time = TIME.clock()
# get number and model 0525-0620 ---0525-0629(new)  data_g + "_" + data_time + "_new.txt"
# get all numbers and models ----models_all.txt $ users_all.txt

file_model = []
for filename in os.listdir(r'/root/puchaoyi/model'):

    file_model.append(filename)
    # print filename

models_all = []
nums_all = []
file_models = open("/root/PycharmProjects/datatestyd/1lastest_data/result/models_all.txt","w")
file_users = open("/root/PycharmProjects/datatestyd/1lastest_data/result/users_all.txt","w")

for filename in file_model:
    print filename
    data_filename = filename.split("_")
    data_g = data_filename[0]
    data_time = data_filename[2]
    result_name = data_g + "_" + data_time + "_new.txt"
    file_result = open("/root/PycharmProjects/datatestyd/1lastest_data/result/" + result_name,"w")
    file_1 = open("/root/puchaoyi/model/" + filename)
    for line in file_1:
        line = line.strip("\n")
        if "|" in line:
            data = line.split("|")
            nums = data[0]
            data_num = nums.split(",")
            num = data_num[0]
            models = data[2]
            data_model = models.split(",")
            model = data_model[0]
            result = num + " " + model
            file_result.write(result)
            file_result.write("\n")
            models_all.append(model)
            nums_all.append(num)
    end_time = TIME.clock()
    print "time: %f s" % (end_time - start_time)
    file_1.close()
    file_result.close()

models_all = list(set(models_all))
nums_all = list(set(nums_all))
for model in models_all:
    file_models.write(model)
    file_models.write("\n")
for num in nums_all:
    file_users.write(num)
    file_users.write("\n")

file_models.close()
file_users.close()
end_time = TIME.clock()
print "time: %f s" % (end_time - start_time)

