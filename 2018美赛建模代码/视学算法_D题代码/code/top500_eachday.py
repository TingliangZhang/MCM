# coding=utf-8   #
# 0526-0610
# top500 user+top500 app_need


import time as TIME

start_time = TIME.clock()

dates = ["526", "527", "528", "529", "530", "531", "601", "602", "603", "604", "605", "606", "607", "608", "609", "610"]

apps_need = ["1", "3", "4", "5", "11", "14"]

for date in dates:
    # filename_1 = "app_20160" + date + "_new.txt"
    filePath_1 = "/root/PycharmProjects/datatestyd/5_lastest_data_app_new/result_5/"
    filename_1 = filePath_1 + "app_20160" + date + "_new.txt"
    print filename_1
    filePath_2 = "/root/PycharmProjects/datatestyd/6_top500_eachday/result_6/"
    filename_result = filePath_2 + "top500_20160" + date + ".txt"
    print filename_result
    # filename_change = "model_20160" + date + "_change.txt"
    print filename_1
    file_1 = open(filename_1, "r")
    file_result = open(filename_result, "w")
    # file_change = open(filename_change,"w")
    users = []
    flows = []
    flows_need = []

    line_no = 0
    for line in file_1:
        line_no += 1
        if line_no % 10000 == 0:
            end_time = TIME.clock()
            print "time: %f s" % (end_time - start_time)
        line = line.strip()
        data = line.split("|")
        app = data[1]
        user = data[2]
        flow = int(data[7]) + int(data[8]) + int(data[9]) + int(data[10])
        if user not in users:
            users.append(user)
            flows.append(flow)
            flows_need.append(0)
        else:
            pos = users.index(user)
            flows[pos] += flow
        if app in apps_need:
            pos = users.index(user)
            flows_need[pos] += flow

    print "finish 11111"
    end_time = TIME.clock()
    print "time: %f s" % (end_time - start_time)
    user_top500 = []
    app_need_top500 = []
    for i in range(500):
        flow = max(flows)
        pos = flows.index(flow)
        user = users[pos]
        user_top500.append(user)
        app_need = apps_need[pos]
        need = round(app_need / flow, 2)
        app_need_top500.append(need)
        del flows[pos]
        del users[pos]
        del flows_need[pos]

    for i in range(500):
        result = user_top500[i] + " " + str(app_need_top500[i])
        print result
        file_result.write(result)
        file_result.write("\n")
    file_1.close()
    file_result.close()
    # file_change.close()
    end_time = TIME.clock()
    print "time: %f s" % (end_time - start_time)
