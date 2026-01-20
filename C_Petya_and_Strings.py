str1 = str(input())
srt2 = str(input())

if str1.lower() < srt2.lower():
    print(-1)
elif str1.lower() > srt2.lower():
    print(1)
else:
    print(0)