# change all years from 2023 to 2024
years = ["January 2023", "May 2025", "April 2023", "August 2024", "September 2025", "December 2023"]

# With for loop

updated_years = []

for year in years:
    if(year.endswith("2023")):
        new = year.replace("2023","2024")
        updated_years.append(new)
    else: updated_years.append(year)

print(updated_years)

# Using list comprehension:

updated_years_1 = [year.replace("2023","2024") if year[-4:]=="2023" else year for year in years]
print(updated_years_1)
    