hrs = raw_input("Enter hours:")
h = float(hrs)
rate = raw_input("Enter rate:")
r = float(rate)

if h > 40:
    basic = 40 * r
    ot = (h - 40) * (r * 1.5)
    pay = basic + ot
else:
    pay = h * r

print pay
