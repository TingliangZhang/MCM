# coding=utf-8   #
import time as TIME

start_time = TIME.clock()

dates = ["526", "527", "528", "529", "530", "531", "601", "602", "603", "604", "605", "606", "607", "608", "609", "610"]
# dates = ["test"]

file_1 = open("/root/PycharmProjects/datatestyd/8_user_error_all/result_8/user_error_all.txt", "r")
dict_error = {}
for line in file_1:
    line = line.strip()
    data = line.split("|")
    user = data[0]
    model = data[1:]
    dict_error[user] = model

file_1.close()

filename_result = "/root/PycharmProjects/datatestyd/10_user_error_all_new/result_10/user_error_all_new.txt"
dict_users = {}
file_result = open(filename_result, "w")
for date in dates:
    filename_1 = "/root/PycharmProjects/datatestyd/9_user_change_all/result_9/" + "model_" + date + "_error_new.txt"
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
            model_old = dict_error[user]
            dict_error[user] = list(set(model_old).union(set(model)))
        except:

            dict_error[user] = []
            dict_error[user] = model

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
for user in dict_error.keys():
    model = dict_error[user]
    result = user + "|" + "|".join(model)
    file_result.write(result)
    file_result.write("\n")

file_result.close()
end_time = TIME.clock()
print "time: %f s" % (end_time - start_time)
