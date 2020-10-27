N = 1260
five_hundred = N // 500
hundred = (N - (five_hundred * 500)) // 100
fifty = (N - (five_hundred * 500) - (hundred * 100)) // 50
ten = (N - (five_hundred * 500) - (hundred * 100) - (fifty * 50)) // 10

print(five_hundred, hundred, fifty, ten)