# coding=utf-8   #
# merge the 3g&4g data in same format: user + model
import time as TIME
start_time = TIME.clock()

dates = ["526","527","528","529","530","531","601","602","603","604","605","606","607","608","609","610"]

for date in dates:
    filePath_1 = "/root/PycharmProjects/datatestyd/1_lastest_data/result_1/"
    filename_1 = filePath_1 + "3g_20160" + date + "_new.txt"
    filename_2 = filePath_1 + "4g_20160" + date + "_new.txt"
    filename_result = "model_20160" + date + ".txt"
    print filename_result
    file_1 = open(filename_1,"r")
    file_2 = open(filename_2,"r")
    file_result = open("/root/PycharmProjects/datatestyd/4_model_3g+4g/result_4/"+filename_result,"w")
    for line in file_1:
        line = line.strip()
        file_result.write(line)
        file_result.write("\n")
    for line in file_2:
        line = line.strip()
        file_result.write(line)
        file_result.write("\n")
    file_1.close()
    file_2.close()
    file_result.close()
    end_time = TIME.clock()
    print "time: %f s" % (end_time - start_time)
