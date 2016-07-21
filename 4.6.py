def computepay(h,r):
    if h < 40:
        pay = h * r
    else:
        base = 40 * r
        ot = (h - 40) * (r * 1.5)
        pay = base + ot
    return pay

hrs = raw_input("Enter Hours:")
h = float(hrs)
rate = raw_input("Enter rate:")
r = float (rate)
p = computepay(h,r)
print p
