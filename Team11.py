with open("hr_system.txt") as hr_file:
    for line in hr_file:
        line = line.strip()
        hr_list = line.split(" ")
        
        name = hr_list[0]
        id_number = hr_list[1]
        title = hr_list[2]
        salary = float(hr_list[3])

        if title.lower() == "engineer":
            print(f"{name} ({id_number}), {title} - ${round(salary / 24 + 1000, 2)}")

        else:
            print(f"{name} ({id_number}), {title} - ${round(salary / 24, 2)}")
