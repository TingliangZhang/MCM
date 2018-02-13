# coding=utf-8   #
import time as TIME

start_time = TIME.clock()

dates = ["526", "527", "528", "529", "530", "531", "601", "602", "603", "604", "605", "606", "607", "608", "609", "610"]
# dates = ["test"]

file_1 = open("/root/PycharmProjects/datatestyd/9_user_change_all/result_9/user_change_all.txt", "r")
dict_change = {}
dict_date = {}
for line in file_1:
    line = line.strip()
    data = line.split("|")
    user = data[0]
    model = data[1:3]
    date = data[3]
    dict_change[user] = model
    dict_date[user] = date

file_1.close()

filename_result = "/root/PycharmProjects/datatestyd/11_user_change_all_new/result_11/user_change_all_new.txt"
dict_users = {}
file_result = open(filename_result, "w")
for date in dates:
    filename_1 = "model_" + date + "_change_new.txt"
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
        model = data[1:3]
        date = data[3]
        # print model
        try:
            model_old = dict_change[user]
            print user
        except:

            dict_change[user] = []
            dict_change[user] = model
            dict_date[user] = date

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
for user in dict_change.keys():
    model = dict_change[user]
    date = dict_date[user]
    result = user + "|" + "|".join(model) + "|" + date
    file_result.write(result)
    file_result.write("\n")

file_result.close()
end_time = TIME.clock()
print "time: %f s" % (end_time - start_time)

