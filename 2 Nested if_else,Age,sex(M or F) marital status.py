age=int(input("enter age"))
sex=input("enter sex")
marital=input("enter marital")
if sex=="f":
    if age>=18 and age<=60:
        print("she will work only urban area")
    else:
        print("non")
elif sex=="m":
    if age>=20 and age<=40:
        print("he may work in only where")
    elif age>=40 and age<=60:
        print("he will work in urban area only")
    else:
        print("not urban area")
else:
    print("eror")