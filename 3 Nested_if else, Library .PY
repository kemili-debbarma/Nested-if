e_day=int(input("enter expected day"))
e_month=int(input("enter expected month"))
e_year=int(input("enter expected month"))
r_day=int(input("enter return day"))
r_month=int(input("enter return month"))
r_year=int(input("enter return year"))
if e_month==r_month and e_year ==r_year:
    if r_day<=e_day:
        print("no fine")
    elif r_day>e_day:
        n_d_l=e_day-e_day
        fine=15*n_d_l
        print("n_d_l=",n_d_l)
        print("fine",fine)
elif r_day>e_day and r_year==e_year:
    if r_month>e_month:
        n_d_l=r_day-e_day
        n_m_l=(r_month-e_month)*30
        n_l=n_m_l-n_d_l
        fine=500*n_l
        print("n_m_l=l=",n_l)
        print("fine=",fine)
    else:
        print("fine charge")
elif r_month==e_month and r_day==e_day:
    if r_year>e_year:
        fixed_fine=10000
        print("fine=",fixed_fine)
    else:
        print("no fixed_fine")
else:
    print("error")