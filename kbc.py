q=[
    [ "what is criteria for cgpa","age","class","marks",4],
    [ "what is criteria for cgpa","age","class","marks",4],
    [ "what is criteria for cgpa","age","class","marks",4],
    [ "what is criteria for cgpa","age","class","marks",4],
    [ "what is criteria for cgpa","age","class","marks",4],
    [ "what is criteria for cgpa","age","class","marks",4],
    [ "what is criteria for cgpa","age","class","marks",4],
    [ "what is criteria for cgpa","age","class","marks",4],
    [ "what is criteria for cgpa","age","class","marks",4],
    ]
pm=[1000,2000,3000,4000,5000,6000,7000,8000,9000]
i=0
money=0
qns=q[i]
for i in range(0,len(q)):
    money=pm[i]
    print(f"question{i} is {q[i]}")
    ans=int(input("enter ur ans:"))   
    if (ans==qns[4]):
        print(f"correct ans,you have won{pm[i]}")
    else:
        print(f"wrong ans!")
        print(f"you have won {pm[i-1]}.rs")
print("hello github")        