with open('input' ,'r') as f:
    data = [n.split(' | ')[1].split() for n in f.read().split('\n') if n]
    flat_list = [i for ii in data for i in ii if len(i) in [2,4,3,7]]
    print(len(flat_list))
