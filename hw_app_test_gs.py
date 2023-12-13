import gspread

gc = gspread.service_account()

sh = gc.open("1KAAiqjpM0FdQ7MaoLJXumxzccL5ddjedPS2tt29n21A")

print(sh.sheet1.get('A1'))
