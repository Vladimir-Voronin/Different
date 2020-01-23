def check_sum_const(ourlist, const):
    check_list = []
    for var in ourlist:
        for check_var in check_list:
            if var + check_var == const:
                print('Result is {} and {}, for index {} and {}'.format(var, check_var, ourlist.index(var),ourlist.index(check_var)))
                return True
            elif var not in check_list and var != check_var:
                check_list.append(var)
        else:
            check_list.append(var)

    return False
                      
    
