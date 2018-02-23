'''
find the next possible time using the subsets of digits in the input.
One digit can be used multiple times.
13:12 => 13:13
13:14 => 13:31
13:15 => 13:31
23:59 => 22:22
23:49 => 22:22
23:11 => 22:22
11:00 => 11:01
'''
def generate(time):
    hours, mins = time.split(":")
    curr_hour = int(hours[0] + hours[1])
    curr_min = int(mins[0] + mins[1])
    digits = [c for c in hours] + [c for c in mins]
    possible_mins = \
        [int(str(d) + str(k))
                for d in digits
                    for k in digits
                        if int(str(d) + str(k)) > curr_min and int(str(d) + str(k)) < 59]
    if possible_mins:
        return "%02d:%02d" %(curr_hour, sorted(possible_mins)[0])
    possible_hours = \
        [int(str(d) + str(k))
                for d in digits
                    for k in digits
                        if int(str(d) + str(k)) > curr_hour and int(str(d) + str(k)) < 23]
    if possible_hours:
        return "%02d:%02d" %(sorted(possible_hours)[0], curr_min)
    return "{}:{}".format("22", "22")

print generate("13:14")
print generate("05:15")
print generate("19:15")
print generate("23:15")
print generate("23:44")
print generate("23:11")
print generate("23:59")
print generate("11:00")
print generate("11:33")
