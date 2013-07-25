import re
st='asd qw1 qwesjbjlbv ug45ou ougu ugyf u43yu i65435  234 5 653ko ku u b'
nmb=re.compile('\d')
print re.findall(nmb,st)
