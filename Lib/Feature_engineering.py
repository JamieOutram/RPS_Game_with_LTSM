import itertools

def grouper(iterable, n, fillvalue=None):
    args = [iter(iterable)] * n
    return itertools.zip_longest(*args, fillvalue=fillvalue)

def create_states(count, keys):            
    states = []
    for i in itertools.product(keys, repeat=count):
        states.append(''.join(i))
    return states

def get_dist(array, order, keys):
    patterns = create_states(order, keys)
    dist = {pat : 0 for pat in patterns}
    rolling_pattern = patterns[0]
    for play in array:
        rolling_pattern = rolling_pattern[1:] + str(play)
        dist[rolling_pattern] += 1
    return dist

def normalise_dist(dist, order, keys):
    #look at all possible next states from each pattern and group
    #for each group subtract minimum count from total 
    groups = [[''.join(pat) + key for key in keys] for pat in itertools.product(keys, repeat=order-1)]
    for group in groups:
        counts = [dist[key] for key in group]
        #Normalize group between 0-1
        for key in group:
            if(max(counts)==min(counts)):
                dist[key] = 0
            else:
                dist[key] = (dist[key]-min(counts))/(max(counts)-min(counts))            
    
    return list(dist.values())
