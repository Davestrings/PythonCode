years = int(input("Enter years: "))
currentpopulation = 307357870

year_seconds = 365 * 24 * 60 * 60
births_a_year = year_seconds / 7
deaths_a_year = year_seconds / 13
immigrants_a_year = year_seconds / 35

estimatedpopulation = years *(currentpopulation + births_a_year + immigrants_a_year - deaths_a_year)

print("Estimated population is :", estimatedpopulation)