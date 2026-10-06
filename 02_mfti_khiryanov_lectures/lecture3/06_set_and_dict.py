s = {
    "Kyrgyzstan",
    "Bishkek",
    "Osh",
    "Jalal-Abad",
    "Chui",
    "Talas",
    "Batken",
    "Issyk-Kul",
    "Talas"
}
s.add("Kazakhstan")
print(s)

for el in s:
    print(el)


d1 = s
d = d1
d.add("Uzbekistan")
print(d)