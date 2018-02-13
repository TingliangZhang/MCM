# coding=utf-8   #
# get apps_all ---->apps_all.txt
import time as TIME
import os
start_time = TIME.clock()

file_model = []
for filename in os.listdir(r'/root/puchaoyi/data'):
    file_model.append(filename)

apps_all = []
file_apps = open("/root/PycharmProjects/datatestyd/2_lastest_data_app/result_2/apps_all.txt","w")

for filename in file_model:
    print filename

    file_1 = open("/root/puchaoyi/data/" + filename)
    for line in file_1:
        #print line
        #print line.decode('utf-8')
        line = line.strip("\n")
        data = line.split(",")
        app = data[3]
        #print app.decode('utf-8')
        apps_all.append(app)
    end_time = TIME.clock()
    print "time: %f s" % (end_time - start_time)
    file_1.close()

apps_all = list(set(apps_all))

for app in apps_all:
    #print app.decode('utf-8')
    file_apps.write(app)
    file_apps.write("\n")

file_apps.close()
end_time = TIME.clock()
print "time: %f s" % (end_time - start_time)
