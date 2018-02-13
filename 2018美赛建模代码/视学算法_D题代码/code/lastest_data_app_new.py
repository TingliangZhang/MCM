# coding=utf-8   #
# get related information: city app user nums_1 nums_2 nums_3 nums_4 flow_1 flow_2 flow_3 flow_4
import time as TIME
import os

start_time = TIME.clock()

file_model = []
for filename in os.listdir(r'/root/puchaoyi/data'):
    file_model.append(filename)
'''
apps_old = []
apps_new = []
file_apps = open("/root/PycharmProjects/datatestyd/2_lastest_data_app/result_2/apps_all.txt.txt","r")
for line in file_apps:
    line = line.strip()
    data = line.split(" ")
    app_old = data[0]
    app_new = data[1]
    apps_old.append(app_old)
    apps_new.append(lapp_new)
file_apps.close()
'''

for filename in file_model:
    print filename
    data_filename = filename.split("_")
    data_time = data_filename[3]
    data_time =data_time.split(".")
    data_time=data_time[0]
    resultPath = "/root/PycharmProjects/datatestyd/5_lastest_data_app_new/result_5/"
    result_name = "app_" + data_time + "_new.txt"
    # print result_name
    file_result = open(resultPath + result_name, "w")

    file_1 = open("/root/puchaoyi/data/" + filename, "r")
    for line in file_1:
        # print line
        # print line.decode('utf-8')
        line = line.strip("\n")
        data = line.split(",")
        city = data[0]
        app = data[3]
        user = data[4]
        nums_1 = data[13]
        nums_2 = data[14]
        nums_3 = data[15]
        nums_4 = data[16]
        flow_1 = data[17]
        flow_2 = data[18]
        flow_3 = data[19]
        flow_4 = data[20]
        # app_pos = apps_old.index(appid)
        # app = apps_new[app_pos]
        result = city + "|" + app + "|" + user + "|" + nums_1 + "|" + nums_2 + "|" + nums_3 + "|" + nums_4 + "|" + flow_1 + "|" + flow_2 + "|" + flow_3 + "|" + flow_4
        file_result.write(result)
        file_result.write("\n")
    file_1.close()
    file_result.close()
    end_time = TIME.clock()
    print "time: %f s" % (end_time - start_time)


