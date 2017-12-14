import datetime
import meal
import deal_json
import material_class
import json

def register_meal():
    print("食事記録を登録しましょう。")
    date = datetime.date.today().strftime("%y/%m/%d")
    while True:
        sort = int(input("1.朝食 2.昼食 3.夕食 4.間食 5.戻る"))
        if 1 <= sort <= 4:
            break
        elif sort == 5:
            print("戻ります。")
            return
        else:
            print("1~4で入力してください")
    materials = {}
    while True:
        cuisine = input("料理名を入力してください。終了する場合はqを入力してください")
        if cuisine == "q":
            break
        materials[cuisine] = {}
        while True:
            mate = input("材料を一つずつ入力してください。終了した場合はqを。")
            if mate == "q":
                break

            advance = search(mate)
            if advance:
                d = input("%sが見つかりました。使いますか？y or n"%advance[0])
                if d == "y":
                    while True:
                        print("食材の量を入力してください(%s単位)"%material_class.change_each(advance[1]))
                        amount = int(input())
                        break
                    calory = advance[2]*amount
                    cost = advance[3]*amount
                    materials[cuisine][mate] = [calory,cost]
                    print("カロリー:%dcal 費用:%d円"%(calory,cost))
                    continue

            try:
                calory = int(input("食材のカロリーを入力してください"))
                cost = int(input("金額を入力してください"))
                materials[cuisine][mate] = [calory,cost]
                continue
            except:
                print("数字で入力してください。もう一度初めから。")
                continue



    dish = meal.Meal(sort,date,materials)
    dish.save()

def view_all_meal():
    print("全ての食事記録を表示します")
    view_data = deal_json.load("meal_log.json")
    for d in view_data:
        print("%s %s Menu:%s カロリー:%dkcal 費用:%s円" %(d[1],meal.change_sort(d[0]),\
        d[2],d[3],d[4]))
    print("End")

def register_materials():
    while True:
        name = input("食材を登録・更新します。食材名を登録してください。終了する場合はqを入力してください")
        if name == "q":
            break
        n = search(name)
        if n:
            d = input("同じ名前の食材がすでに登録されています。更新しますか？")
            if d == "y":
                before_data = deal_json.load("materials.json")
                del before_data[n[4]]
                file = open("materials.json","w")
                json.dump(before_data,file)
                file.close()

            else:
                continue
        try:
            while True:
                stan = int(input("1.1個(杯)当たり 2.1g当たり"))
                if 1 <= stan <= 2:
                    break
                print("正しく入力してください")
            per_calory = int(input("カロリーを入力してください"))
            per_cost = int(input("値段を入力してください"))
        except:
            print("数字で入力してください。初めから。")
            continue

        material_class.Materials(name,stan,per_calory,per_cost)

def search(keyword):
    json_file = deal_json.load("materials.json")
    num = 0
    for i in json_file:
        if keyword == i[0]:
            i.append(num)
            return i
        num += 1
    return None
