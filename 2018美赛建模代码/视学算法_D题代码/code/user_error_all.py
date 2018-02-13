# coding=utf-8   #
# try except?
# can not understand
# emerge all error_users(Duplicate removal)

import time as TIME

start_time = TIME.clock()

dates = ["526", "527", "528", "529", "530", "531", "601", "602", "603", "604", "605", "606", "607", "608", "609", "610"]
# dates = ["test"]

filename_result = "/root/PycharmProjects/datatestyd/8_user_error_all/result_8/"+"user_error_all.txt"
dict_users = {}
file_result = open(filename_result, "w")
for date in dates:
    filename_1 = "/root/PycharmProjects/datatestyd/7_model_3g+4g_new/result_7/" + "model_20160" + date + "_error.txt"
    print filename_1
    file_1 = open(filename_1, "r")

    line_no = 0
    for line in file_1:
        line_no += 1
        if line_no % 10000 == 0:
            end_time = TIME.clock()
            print "time: %f s" % (end_time - start_time)
        line = line.strip()
        data = line.split("|")
        user = data[0]
        model = data[1:]
        # print model
        try:
            model_old = dict_users[user]
            dict_users[user] = list(set(model_old).union(set(model)))
        except:

            dict_users[user] = []
            dict_users[user] = model

    print "finish 11111"
    end_time = TIME.clock()
    print "time: %f s" % (end_time - start_time)

    # users_num = len(dict_users.keys())


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

    end_time = TIME.clock()
    print "time: %f s" % (end_time - start_time)
for user in dict_users.keys():
    model = dict_users[user]
    result = user + "|" + "|".join(model)
    file_result.write(result)
    file_result.write("\n")

file_result.close()
end_time = TIME.clock()
print "time: %f s" % (end_time - start_time)
