import func

while True:
    d = int(input("\n----------\n1.食事記録\n2.食材登録\n3.記録表示\n4.終了\n----------\n"))
    if d == 1:
        func.register_meal()
    elif d == 2:
        func.register_materials()
    elif d == 3:
        func.view_all_meal()
    elif d == 4:
        print("終了します")
        break
    else:
        continue
