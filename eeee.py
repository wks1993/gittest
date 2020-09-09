class one(object):
    def __init__(self, city_en, city_cn):
        self.city_en = city_en
        self.city_cn = city_cn

a=one('china','中国')
# ss='city_en'
# print(getattr(a, ss))

class IPC(object):
    def get(self):
        print(self.getres('city_cn'))

    def getres(self, city_type):
        res = getattr(a, city_type)
        return res









