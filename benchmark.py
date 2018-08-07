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

false_pos = -1
true_pos = -1
tolerance = ""
first_time = True

filepath = './result.txt'  
with open(filepath) as fp:  
    for cnt, line in enumerate(fp):
        if(is_header(line)):
            if first_time:
                first_time = False
            else:
                with open('tolerance_exp.csv', 'a') as the_file:
                    the_file.write("%s,%i,%i\n" % (tolerance,true_pos,false_pos))
            false_pos = 0
            true_pos = 0
            tolerance = (line.split(",")[1][:-1])
        else:
           if check_log(line):
               true_pos += 1
           else:
               false_pos += 1

with open('tolerance_exp.csv', 'a') as the_file:
    the_file.write("%s,%i,%i\n" % (tolerance,true_pos,false_pos))

