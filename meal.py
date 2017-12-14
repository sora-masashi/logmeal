import deal_json
class Meal:
    def __init__(self,sort,date,materials):
        #materials is dict of material. 0
        self.sort = sort
        #int data  1..breakfast 2..lunch 3..dinner 4..snack 1
        self.date = date
        #int data  example:2017/12/13 2
        self.menu = list(materials.keys())
        self.sum_calory = 0
        for m in list(materials.values()):
            for i in m.values():
                self.sum_calory += i[0]

        #int data   4
        self.sum_cost = 0
        for m in materials.values():
            for i in m.values():
                self.sum_cost += i[1]

        materials_list = []
        for m in list(materials.values()):
            for i in m.keys():
                materials_list.append(i)
        print(materials_list)

        #int data 5
        self.data_list = [self.sort,self.date,self.menu,self.sum_calory,self.sum_cost,materials_list]



    def save(self):
        deal_json.awrite(self.data_list,"meal_log.json")
        print("Successfully recorded!")
        print("[%s %s]\nMenu:%s\nカロリー:%dkcal\n費用:%s円" %(self.date,change_sort(self.sort),\
        self.menu,self.sum_calory,self.sum_cost))

def change_sort(sort):
    if sort == 1:
        return "朝食"
    elif sort == 2:
        return "昼食"
    elif sort == 3:
        return "夕食"
    elif sort == 4:
        return "間食"
    else:
        return "Error!"
