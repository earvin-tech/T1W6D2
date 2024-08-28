# Create an email format using full name and string methods

full_name = input("Enter your full name:")

company_name = input("Enter your company name:")

# splitted_full_name = full_name.split()
# joined_full_name_with_dot = ".".join(splitted_full_name)
# splitted_company_name = company_name.split()
# joined_company_name = "".join(splitted_company_name)

joined_full_name_with_dot = full_name.replace(" ",".")
joined_company_name = company_name.replace(" ","")

predicted_email = f"{joined_full_name_with_dot}@{joined_company_name}.com.au".lower()

print(predicted_email)