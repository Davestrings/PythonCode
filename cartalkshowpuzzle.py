
for milage in range(10_000,1_000_000):
    milage_str = str(milage)
    last_four= milage_str[2:6]
    last_five = milage_str[-5:]
    if(last_four == last_four[::-1]) and (last_five != last_five[::-1]):
        milage_str = str(milage + 1)
        last_five = milage_str[-5:]

        if(last_five == last_five[::-1]):
            milage_str = str(milage + 2)
            mid_four = milage_str[1:5]

            if(mid_four == mid_four[::-1]):
                milage_str = str(milage + 3)

                if(milage_str == milage_str[::-1]):
                    print(f"the mile is ={milage}")
