def fact():
    num = int(input("Enter the Number :"))
    ans=num
    for i in range(1,ans):
        ans=ans*i;
    print("Factorial of ",num,"is",ans)

fact()