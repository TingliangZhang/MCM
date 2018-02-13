# coding=utf-8   #
#
# model_ret = list(set(model) ^ set(model_old))
# ??? can't understand
import time as TIME

start_time = TIME.clock()

dates = ["526", "527", "528", "529", "530", "531", "601", "602", "603", "604", "605", "606", "607", "608", "609", "610"]
# dates = ["test"]

file_1 = open("/root/PycharmProjects/datatestyd/8_user_error_all/result_8/user_error_all.txt", "r")
user_error = []
for line in file_1:
    line = line.strip()
    data = line.split("|")
    user = data[0]
    user_error.append(user)
lenth_1 = len(user_error)
lenth_2 = len(set(user_error))
print lenth_1, lenth_2
file_1.close()

filename_result = "/root/PycharmProjects/datatestyd/9_user_change_all/result_9/user_change_all.txt"
dict_users = {}
dict_dates = {}
file_result = open(filename_result, "w")
for date in dates:
    filename_1 = "/root/PycharmProjects/datatestyd/7_model_3g+4g_new/result_7/model_20160" + date + "_change.txt"
    print filename_1
    file_1 = open(filename_1, "r")
    filename_error_new = "/root/PycharmProjects/datatestyd/9_user_change_all/result_9/model_" + date + "_error_new.txt"
    file_error = open(filename_error_new, "w")

    line_no = 0
    no_error = 0
    for line in file_1:
        line_no += 1
        if line_no % 10000 == 0:
            end_time = TIME.clock()
            print "time: %f s" % (end_time - start_time)
        line = line.strip()
        data = line.split("|")
        user = data[0]
        if user not in user_error:
            model = data[1:]
            try:
                model_old = dict_users[user]
                if set(model) == set(model_old):
                    dict_dates[user] = date
                else:
                    model_ret = list(set(model) ^ set(model_old))
                    label = 1
                    for item in model_ret:
                        if "iPhone" not in item:
                            label = 0
                            break
                    if label == 1:
                        model_ret = max(model_ret)
                        if model_ret in model:
                            dict_users[user] = model
                    else:
                        user_error.append(user)
                        no_error += 1
                        model = list(set(model + model_old))
                        result = user + "|"
                        result = result + "|".join(model)
                        file_error.write(result)
                        file_error.write("\n")
                        del dict_users[user]
                        del dict_dates[user]
            except:
                dict_users[user] = model
                dict_dates[user] = date

    print no_error
    print "finish 11111"

    file_1.close()
    file_error.close()

    end_time = TIME.clock()
    print "time: %f s" % (end_time - start_time)
for user in dict_users.keys():
    model = dict_users[user]
    date = dict_dates[user]
    result = user + "|" + "_".join(model) + "|" + date
    file_result.write(result)
    file_result.write("\n")

file_result.close()
end_time = TIME.clock()
print "time: %f s" % (end_time - start_time)

