balance = 2250
interestRate = .045
term = 120

month = 0

while month < term:
    monthReport = month + 1
    print("Month: ", monthReport, "\t", "Interest Earned: $", balance * (interestRate / 12), "New Balance: $", balance + (balance * (interestRate / 12)))
    balance = balance + (balance * (interestRate / 12))
    month = month + 1
