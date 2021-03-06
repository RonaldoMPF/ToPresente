def check_log(recognition_log):
    pair = recognition_log.split(",")
    filename_tested = pair[0].split("/")[-1]
    filename_result = pair[1].split("/")[-1]
    no_extension_tested = filename_tested.split(".")[0] 
    no_extension_result = filename_result.split(".")[0] 
    check = no_extension_tested == no_extension_result
    return check

def is_header(recognition_log):
    pair = recognition_log.split(",")
    is_header = pair[0] == "tolerance"
    return is_header

#example = "./data/test/9326871.20.jpg,9326871.1"
#example2 = "./data/test/ajones.4.jpg,9338446.1"
#print(example2 + " " + str(check_log(example2)))


false_pos = -1
true_pos = -1
tolerance = -1
first_time = True

filepath = 'res.txt'  
with open(filepath) as fp:  
    for cnt, line in enumerate(fp):
        if(is_header(line)):
            if first_time:
                first_time = False
            else:
                with open('tolerance_exp.csv', 'a') as the_file:
                    the_file.write("%i,%i,%i\n" % (tolerance,true_pos,false_pos))
            false_pos = 0
            true_pos = 0
            tolerance = int(line.split(",")[1])
        else:
           if check_log(line):
               true_pos += 1
           else:
               false_pos += 1

with open('tolerance_exp.csv', 'a') as the_file:
    the_file.write("%i,%i,%i\n" % (tolerance,true_pos,false_pos))

