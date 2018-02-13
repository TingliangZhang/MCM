# coding=utf-8   #
# class unchange len=1; change len=2; else error

import time as TIME

start_time = TIME.clock()

dates = ["526", "527", "528", "529", "530", "531", "601", "602", "603", "604", "605", "606", "607", "608", "609", "610"]
# dates = ["test"]

for date in dates:
    filename_1 = "/root/PycharmProjects/datatestyd/4_model_3g+4g/result_4/" + "model_20160" + date + ".txt"
    filename_result = "/root/PycharmProjects/datatestyd/7_model_3g+4g_new/result_7/" + "model_20160" + date + "_unchange.txt"
    filename_change = "/root/PycharmProjects/datatestyd/7_model_3g+4g_new/result_7/" + "model_20160" + date + "_change.txt"
    filename_error = "/root/PycharmProjects/datatestyd/7_model_3g+4g_new/result_7/" + "model_20160" + date + "_error.txt"
    print filename_1
    file_1 = open(filename_1, "r")
    file_result = open(filename_result, "w")
    file_change = open(filename_change, "w")
    file_error = open(filename_error, "w")
    dict_users = {}

    line_no = 0
    for line in file_1:
        line_no += 1
        if line_no % 10000 == 0:
            end_time = TIME.clock()
            print "time: %f s" % (end_time - start_time)
        line = line.strip()
        data = line.split(" ", 1)
        user = data[0]
        model = data[1]
        if "iPad" not in model and "PAD" not in model and "µçÊÓ" not in model:
            # print model
            try:
                model_old = dict_users[user]
                temp = 0
                for item in model_old:
                    pos = model_old.index(item)
                    if "iPhone" in item and "iPhone" in model:
                        dict_users[user][pos] = max(model, model_old)
                        temp = 1
                        break
                    elif item in model:
                        dict_users[user][pos] = model
                        temp = 1
                        break
                if temp == 0:
                    dict_users[user].append(model)
            except:

                dict_users[user] = []
                dict_users[user].append(model)

    print "finish 11111"
    end_time = TIME.clock()
    print "time: %f s" % (end_time - start_time)

    # users_num = len(dict_users.keys())
    for user in dict_users.keys():
        model = dict_users[user]
        if len(model) == 1:
            result = user + "|" + "|".join(model)
            file_result.write(result)
            file_result.write("\n")
        elif len(model) == 2:
            result = user + "|" + "|".join(model)
            file_change.write(result)
            file_change.write("\n")
        else:
            lenth = len(model)
            result = user + "|" + "|".join(model)
            result = result.strip("|")
            file_error.write(result)
            file_error.write("\n")

    '''
    print "finish 22222"
    end_time = TIME.clock()
    print "time: %f s" % (end_time - start_time)

    users_change_num = len(users_change)
    for i in range(users_change_num):
        user = users_change[i]
        model_old = models_old[i]
        model_new = models_new[i]
        result = user + " " + model_old + " " + model_new
        file_change.write(result)
        file_change.write("\n")
    '''

    file_1.close()
    file_result.close()
    file_change.close()
    file_error.close()
    end_time = TIME.clock()
    print "time: %f s" % (end_time - start_time)
