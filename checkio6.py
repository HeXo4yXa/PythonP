'''
checkio([[
'X...',
'..X.',
'X..X',
'....'],[
'itdf',
'gdce',
'aton',
'qrdi']
])
'''

def checkio(input_data):
    'Return password of given cipher map'
    #print input_data[0], input_data[1]
    id=input_data[1]
    finaltxt=''
    gr=input_data[0]
    for r in range(4):
        #print gr
        for i in range(4):
            for y in range(4):
                if list(gr[i])[y] == 'X':
                    finaltxt+=id[i][y]
        gr=ndegr(gr)
    return finaltxt

def ndegr(dd):
    ddr=['','','','']
    d=len(dd)
    tstr=''
    for i in range(d):
        for y in range(d-1,-1,-1):
            #print i,y, list(dd[y])[i]
            tstr+=list(dd[y])[i]
        ddr[i]+=tstr
        tstr=''
    return ddr

print checkio([[
'X...',
'..X.',
'X..X',
'....'
],[
'itdf',
'gdce',
'aton',
'qrdi'
]
])