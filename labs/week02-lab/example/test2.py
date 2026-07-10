print("2. Time Converter:")
print("   - Ask user for seconds")
print("   - Convert to hours, minutes, and remaining seconds")
print("   - Example: 3661 seconds = 1 hour, 1 minute, 1 second")
print()

s = int(input("enter seconds = "))

h = s // 3600
Sr = s % 3600

m = Sr // 60
Sr = m * 60



print("totoal hour = ",h)
print("totoal min = ",m)
print("totoal sec = ",s)

