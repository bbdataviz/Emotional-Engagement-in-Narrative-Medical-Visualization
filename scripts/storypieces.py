
def storypieces(a,s):
    atom_h = a[0]
    atom_m = a[1]
    atom_s = a[2]
    eye0_m = a[3]
    eye0_s = a[4]
    step_m = 5
    step_s = 6
    final = []

    for i in range (1, int((len(a)-2)/2)):
        # calculate difference
        if(eye0_s > a[step_s]):
            diff_min = a[step_m] - eye0_m - 1
            diff_sec = 60 - eye0_s + a[step_s]
        else: 
            diff_sec = a[step_s] - eye0_s
            diff_min = a[step_m] - eye0_m

        # calculate sum => clock
        if(atom_s + diff_sec > 59):
            min = atom_m + diff_min + 1
            sec = atom_s + diff_sec - 60
        else:
            min = atom_m + diff_min
            sec = atom_s + diff_sec
        
        if(min > 59): 
            hours = atom_h + 1
            min = min - 60
        else:
            hours = atom_h
        # Cache
        save = [i+s, hours, min, sec]
        # Add to final array (clocktimes)
        final.append(save)

        # next story piece    
        step_m = step_m + 2
        step_s = step_s + 2

    return final 

# convert into 'hh:mm:ss' format
def storypieces_convert(a,s):
    atom_h = a[0]
    atom_m = a[1]
    atom_s = a[2]
    eye0_m = a[3]
    eye0_s = a[4]
    step_m = 5
    step_s = 6
    final = []

    for i in range (1, int((len(a)-2)/2)):
        # calculate difference
        if(eye0_s > a[step_s]):
            diff_min = a[step_m] - eye0_m - 1
            diff_sec = 60 - eye0_s + a[step_s]
        else: 
            diff_sec = a[step_s] - eye0_s
            diff_min = a[step_m] - eye0_m

        # calculate sum => clock
        if(atom_s + diff_sec > 59):
            min = atom_m + diff_min + 1
            sec = atom_s + diff_sec - 60
        else:
            min = atom_m + diff_min
            sec = atom_s + diff_sec
        
        if(min > 59): 
            hours = atom_h + 1
            min = min - 60
        else:
            hours = atom_h
        
        # add a 0 infront of a single digit, e.g., 12:3:4 => 12:03:04
        zero = '0'
        sec = str(sec)
        if len(sec) == 1:
            sec = zero + sec
        
        min = str(min)
        if len(min) == 1:
            min = zero + min

        # Cache
        clock = str(hours)+":"+ str(min)+":"+ str(sec)
        save = [i+s, clock]
        # Add to final array (clocktimes)
        final.append(save)

        # next story piece    
        step_m = step_m + 2
        step_s = step_s + 2

    return final 

# convert into 'hh:mm:ss' format
def storypieces_convert_handlejumps(a, storypieces):
    atom_h = a[0]
    atom_m = a[1]
    atom_s = a[2]
    eye0_m = a[3]
    eye0_s = a[4]
    step_m = 5
    step_s = 6
    final = []

    for i in range (1, int((len(a)-2)/2)):
        # calculate difference
        if(eye0_s > a[step_s]):
            diff_min = a[step_m] - eye0_m - 1
            diff_sec = 60 - eye0_s + a[step_s]
        else: 
            diff_sec = a[step_s] - eye0_s
            diff_min = a[step_m] - eye0_m

        # calculate sum => clock
        if(atom_s + diff_sec > 59):
            min = atom_m + diff_min + 1
            sec = atom_s + diff_sec - 60
        else:
            min = atom_m + diff_min
            sec = atom_s + diff_sec
        
        if(min > 59): 
            hours = atom_h + 1
            min = min - 60
        else:
            hours = atom_h
        
        # add a 0 infront of a single digit, e.g., 12:3:4 => 12:03:04
        zero = '0'
        sec = str(sec)
        if len(sec) == 1:
            sec = zero + sec
        
        min = str(min)
        if len(min) == 1:
            min = zero + min

        # Cache
        clock = str(hours)+":"+ str(min)+":"+ str(sec)
        save = [storypieces[i-1], clock]
        # Add to final array (clocktimes)
        final.append(save)

        # next story piece    
        step_m = step_m + 2
        step_s = step_s + 2

    return final 




