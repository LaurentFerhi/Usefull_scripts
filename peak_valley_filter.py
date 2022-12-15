def remove_intermediate(l):
    if (l[-1]-l[-2])*(l[-2]-l[-3]) >= 0:
        del(l[-2])
    return l

def process_signal(signal):

    l = [0] # init list with first 0

    for i in range(len(signal)):
        
        l +=[signal[i]] # populate list

        if len(l) >= 3:
            remove_intermediate(l)
            
    l += [0] # add 0 at the end of the list
    remove_intermediate(l)

    return l