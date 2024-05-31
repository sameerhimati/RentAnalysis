def grossRent(RentPerUnit, NumUnits):
    return RentPerUnit * NumUnits

def OperatingExpenses(Taxes, Insurance, Utilities, 
                      Maintenance, Management, Other):
    return Taxes + Insurance + Utilities + Maintenance + Management + Other

def OperatingExpenseEstimate(grossRent):
    return grossRent * 0.5  # 50% of gross rent

def netOperatingIncome(GrossIncome, OperatingExpenses):
    return GrossIncome - OperatingExpenses

def cashFlow(NetOperatingIncome, DebtService):
    return NetOperatingIncome - DebtService # DebtService is the mortgage payment

def cashOnCashReturn(AnnualCashFlow, TotalCashInvested):
    return AnnualCashFlow / TotalCashInvested

def capRate(NetOperatingIncome, PurchasePrice):
    return (NetOperatingIncome * 12) / PurchasePrice

def interiorRepairs(Demo=0, Plumbing=0, Electrical=0, HVAC=0, Drywall=0, 
                    Flooring=0, Painting=0, Materials=0, Other=0):
    return Demo + Plumbing + Electrical + HVAC + Drywall + Flooring \
        + Painting + Materials + Other

def exteriorRepairs(Roof=0, Siding=0, Windows=0, Doors=0, 
                    Foundation=0, Landscaping=0, Other=0):
    return Roof + Siding + Windows + Doors + Foundation + Landscaping + Other

def RenovationCosts(Interior=0, Exterior=0, Other=0):
    return Interior + Exterior + Other

def projectCost(PurchasePrice, ClosingCosts, RenovationCosts, 
                preRentHoldingCosts):
    return PurchasePrice + ClosingCosts + RenovationCosts + \
        preRentHoldingCosts


def propertyAnalysis():
    # Property Information
    purchasePrice = 100000
    closingCosts = 5000

    # InteriorRepairs
    Demo = 1000
    Plumbing = 500
    Electrical = 500
    HVAC = 1000
    Drywall = 500
    Flooring = 2000
    Painting = 1000
    Materials = 1000
    otherInterior = 500

    # ExteriorRepairs
    Roof = 2000
    Siding = 2000
    Windows = 1000
    Doors = 500
    Foundation = 1000
    Landscaping = 500
    otherExterior = 500
    
    # Project Info
    projectedRent = 1000
    units = 1

    totalRent = grossRent(projectedRent, units)
    projectTimeMonths = 6

    Interior = interiorRepairs(Demo, Plumbing, Electrical, HVAC, 
                               Drywall, Flooring, Painting, Materials, 
                               otherInterior)
    Exterior = exteriorRepairs(Roof, Siding, Windows, Doors, 
                               Foundation, Landscaping, otherExterior)

    renovationCosts = RenovationCosts(Interior, Exterior)

    preRentHoldingCosts = projectedRent * projectTimeMonths

    # Step 1: Project Cost
    projectCost = projectCost(purchasePrice, closingCosts, renovationCosts,
                               preRentHoldingCosts)
    
    # Step 2: Financing & Total Out of Pocket
    downPaymentPercent = 0.2
    LTV = 1 - downPaymentPercent
    loanAmount = LTV * purchasePrice

    cashNeeded = projectCost - loanAmount

    # Step 3: Monthly Mortgage Payment

    loanPeriodYears = 30
    interestRate = 0.05
    monthlyLoanPayment = loanAmount * (interestRate / 12) / \
        (1 - (1 + interestRate / 12) ** (-loanPeriodYears * 12))

    # monthlyLoanPayment = 3100

    # Step 4: Total Income

    grossIncome = grossRent(projectedRent, units=1)

    # Step 5: Operating Expenses

    taxes = 1000
    insurance = 500
    utilities = 500
    maintenance = 500
    management = 500
    other = 500

    operatingExpenses = OperatingExpenses(taxes, insurance, utilities,
                                            maintenance, management, other)
    
    totalOperatingExpenses = ((OperatingExpenseEstimate(grossIncome)\
                               + operatingExpenses) / 2) + monthlyLoanPayment
    
    # Step 6: Net Operating Income

    netOperatingIncome = netOperatingIncome(grossIncome, totalOperatingExpenses)

    # Step 7: Cash Flow

    cashFlow = cashFlow(netOperatingIncome, monthlyLoanPayment)

    # Step 8: Cash on Cash Return

    cashOnCashReturn = cashOnCashReturn(cashFlow, cashNeeded)

    # Step 9: Cap Rate

    realCapRate = capRate(netOperatingIncome, projectCost)
    CapRate = capRate(netOperatingIncome, purchasePrice)
    
    # Step 10: Return on Investment
    propertyHoldTimeYears = 5
    projectedAppreciation = 0.03
    projectedSalesPrice = purchasePrice * (1 + projectedAppreciation) ** propertyHoldTimeYears

    salesExpense = 5000

    loanBalance = loanAmount - (loanAmount * (1 + interestRate) ** propertyHoldTimeYears)
    # loanBalance = 0

    totalProfit = projectedSalesPrice - loanBalance - salesExpense - cashNeeded

    ROI = (totalProfit / cashNeeded) / propertyHoldTimeYears

    return {
        'projectCost': projectCost,
        'cashNeeded': cashNeeded,
        'monthlyLoanPayment': monthlyLoanPayment,
        'grossIncome': grossIncome,
        'totalOperatingExpenses': totalOperatingExpenses,
        'netOperatingIncome': netOperatingIncome,
        'cashFlow': cashFlow,
        'cashOnCashReturn': cashOnCashReturn,
        'realCapRate': realCapRate,
        'CapRate': CapRate,
        'ROI': ROI
    }

if __name__ == '__main__':
    print(propertyAnalysis())
