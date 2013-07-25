class comp(dict):
    def __init__(self, *args, **kwds):
        super(comp, self).__init__(*args, **kwds)
        self.__dict__ = self

c=comp
pc=c(monitor=c(name="LG"), tastatura=c(name="A4tech"), mouse=c(name="Logitech"), blocsys=c(motherboard=c(name="Asustech", chipset="AMD71", procesor=c(name="Intel", frecGhz=3200), cooler="Glacial"), hdd=c(quant=2, vol=500, mes="Gb", name="Seagate"), ram=c(quant=2, vol=2, mes="Gb")))


print pc
