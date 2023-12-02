def extract_names(full_name):
    names = full_name.split()

    first_name  = names[0]
    middle_name = " "
    last_name   = " "
    if len(names)>2:
        middle_name = names[1]
        last_name   = " ".join(names[2:])
    elif len(names) == 2:
        last_name   = names[1]

    return first_name,middle_name,last_name

full_name =input("Enter Your Full Name : ")
first_name,middle_name,last_name = extract_names(full_name)

print(f'\nFirst Name :{first_name}')
print(f'Middle Name:{middle_name}')
print(f'Last Name  :{last_name} \n')
