def RPS_encode_dataframe(df):
    df = df.replace('R', 0)
    df = df.replace('P', 1)
    df = df.replace('S', 2)
    return df

def RPS_encode(char):
    if char == 'R':
        return 0
    elif char == 'P':
        return 1
    elif char == 'S':
        return 2
    
def RPS_decode(num):
    if num == 0:
        return 'R'
    elif num == 1:
        return 'P'
    elif num == 2:
        return 'S'
        
RPSpair_lookup = ['RR','RP','RS','PR','PP','PS','SR','SP','SS']
RPSpair_reverse_lookup = {}
for x in range(len(RPSpair_lookup)):
    RPSpair_reverse_lookup[RPSpair_lookup[x]] = x

def RPSpair_encode(string):
    return RPSpair_reverse_lookup[string]    

def RPSpair_decode(index):
    return RPSpair_lookup[index]
    
def RPSpair_encode_series(series):
    return series.map(lambda x: RPSpair_encode(x))