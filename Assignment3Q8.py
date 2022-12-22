Set1= {1, 2, 3, 4, 5}
Set2= {2, 4, 6, 8}
Set3= {1, 5, 9, 13, 17}
#a.
Set4 = Set1 ^ Set2
print(sorted(Set4))
#b.
Set4 = Set1 ^ Set2 ^ Set3
print(sorted(Set4))
#c.
Set4 = (Set1 & Set2) ^ (Set2 & Set3) ^ (Set1 & Set3)
print(sorted(Set4))
#d.
Set4 = set(range(1, 11)) - Set1
print(sorted(Set4))
#e.
Set4 = set(range(1, 11)) - (Set1 | Set2 | Set3 )
print(sorted(Set4))
