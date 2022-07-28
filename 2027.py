''' 
#++++
+#+++
++#++
+++#+
++++#
''' #이거출력하기

for i in range(5):
    for x in range(5):
        if i == x: # 같은 숫자면 #
            print('#',end ='')
        else: #아니면 + 출력
            print('+',end ='')
    print()