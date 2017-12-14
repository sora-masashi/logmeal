import deal_json

class Materials:
    def __init__(self,name,stan,per_calory,per_cost):
        self.name = name
        self.stan = stan
        self.per_calory = per_calory
        self.per_cost = per_cost

        save_data = [self.name,self.stan,self.per_calory,self.per_cost]
        deal_json.awrite(save_data,"materials.json")
        print("Successfully recorded!")
        print("品名:%s　費用:%d円 カロリー:%dkcal (%sあたり)" %(self.name,self.per_cost,self.per_calory,change_each(self.stan)))




def change_each(stan):
    if stan == 1:
        return "個"
    elif stan == 2:
        return "10g"
    else:
        print("Error!")
