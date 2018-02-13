# coding=utf-8   #
# apps_class
import time as TIME
start_time = TIME.clock()

file_1 = open("/root/puchaoyi/apps_all.txt","r")
file_result_0 = open("/root/PycharmProjects/datatestyd/3_apps_class/result_3/apps_class00.txt","w")
file_result_1 = open("/root/PycharmProjects/datatestyd/3_apps_class/result_3/apps_class_1.txt","w")
file_result_2 = open("/root/PycharmProjects/datatestyd/3_apps_class/result_3/apps_class_2.txt","w")
file_result_3 = open("/root/PycharmProjects/datatestyd/3_apps_class/result_3/apps_class_3.txt","w")
file_result_4 = open("/root/PycharmProjects/datatestyd/3_apps_class/result_3/apps_class_4.txt","w")
file_result_5 = open("/root/PycharmProjects/datatestyd/3_apps_class/result_3/apps_class_5.txt","w")
file_result_6 = open("/root/PycharmProjects/datatestyd/3_apps_class/result_3/apps_class_6.txt","w")
file_result_7 = open("/root/PycharmProjects/datatestyd/3_apps_class/result_3/apps_class_7.txt","w")
file_result_8 = open("/root/PycharmProjects/datatestyd/3_apps_class/result_3/apps_class_8.txt","w")
file_result_9 = open("/root/PycharmProjects/datatestyd/3_apps_class/result_3/apps_class_9.txt","w")
file_result_10 = open("/root/PycharmProjects/datatestyd/3_apps_class/result_3/apps_class_10.txt","w")
file_result_11 = open("/root/PycharmProjects/datatestyd/3_apps_class/result_3/apps_class_11.txt","w")
file_result_12 = open("/root/PycharmProjects/datatestyd/3_apps_class/result_3/apps_class_12.txt","w")
file_result_13 = open("/root/PycharmProjects/datatestyd/3_apps_class/result_3/apps_class_13.txt","w")
file_result_14 = open("/root/PycharmProjects/datatestyd/3_apps_class/result_3/apps_class_14.txt","w")
file_result_15 = open("/root/PycharmProjects/datatestyd/3_apps_class/result_3/apps_class_15.txt","w")
file_result_16 = open("/root/PycharmProjects/datatestyd/3_apps_class/result_3/apps_class_16.txt","w")
file_result_17 = open("/root/PycharmProjects/datatestyd/3_apps_class/result_3/apps_class_17.txt","w")
file_result_18 = open("/root/PycharmProjects/datatestyd/3_apps_class/result_3/apps_class_18.txt","w")


for line in file_1:
    line = line.strip()
    data = line.split(" ")
    app = data[0]
    class_data = data[1]
    if class_data == "00":
        file_result_0.write(line)
        file_result_0.write("\n")
    if class_data == "1" :
        file_result_1.write(app)
        file_result_1.write("\n")
    elif class_data == "2" :
        file_result_2.write(app)
        file_result_2.write("\n")
    elif class_data == "3" :
        file_result_3.write(app)
        file_result_3.write("\n")
    elif class_data == "4" :
        file_result_4.write(app)
        file_result_4.write("\n")
    elif class_data == "5" :
        file_result_5.write(app)
        file_result_5.write("\n")
    elif class_data == "6" :
        file_result_6.write(app)
        file_result_6.write("\n")
    elif class_data == "7" :
        file_result_7.write(app)
        file_result_7.write("\n")
    elif class_data == "8" :
        file_result_8.write(app)
        file_result_8.write("\n")
    elif class_data == "9" :
        file_result_9.write(app)
        file_result_9.write("\n")
    elif class_data == "10" :
        file_result_10.write(app)
        file_result_10.write("\n")
    elif class_data == "11" :
        file_result_11.write(app)
        file_result_11.write("\n")
    elif class_data == "12" :
        file_result_12.write(app)
        file_result_12.write("\n")
    elif class_data == "13" :
        file_result_13.write(app)
        file_result_13.write("\n")
    elif class_data == "14" :
        file_result_14.write(app)
        file_result_14.write("\n")
    elif class_data == "15" :
        file_result_15.write(app)
        file_result_15.write("\n")
    elif class_data == "16" :
        file_result_16.write(app)
        file_result_16.write("\n")
    elif class_data == "17" :
        file_result_17.write(app)
        file_result_17.write("\n")
    elif class_data == "18" :
        file_result_18.write(app)
        file_result_18.write("\n")
    else:
        print app

file_1.close()
file_result_0.close()
file_result_1.close()
file_result_2.close()
file_result_3.close()
file_result_4.close()
file_result_5.close()
file_result_6.close()
file_result_7.close()
file_result_8.close()
file_result_9.close()
file_result_10.close()
file_result_11.close()
file_result_12.close()
file_result_13.close()
file_result_14.close()
file_result_15.close()
file_result_16.close()
file_result_17.close()
file_result_18.close()

end_time = TIME.clock()
print "time: %f s" % (end_time - start_time)
