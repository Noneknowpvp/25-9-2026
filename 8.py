gia = float(input())
sl = float(input())
giam = float(input())
thue = float(input())
tong = gia * sl
sau_giam= tong * (1 - giam/100)
thanh_toan = sau_giam * (1 + thue/100)
print("Thanh toán", thanh_toan)
