from datetime import date

today = date.today()

date = today.strftime("%m/%d")


def main():
    data = []
    trains = []
    output = []
    total_count = 0

    print("Input all your bugs for the week, and type \"get bug list\"")

    while True:
        line = input("")

        if line.lower() == "get bug list":
            break

        data.append(line)

    print()
    print("=" * 100)
    print("Here is HK weekly bug list for / - {} : ".format(date))

    for line in data:
        if "confidential" in line:
            if "rdar" in line:
                tips_segment = line.split("(")
                tips_segment = tips_segment[1].split(":")
                train = tips_segment[0].replace("[", "").replace("]", "")

                if train.strip() not in trains:
                    trains.append(train.strip())

        elif "confidential" in line:
            train = "confidential"

            if train.strip() not in trains:
                trains.append(train.strip())

        elif "rdar://" in line:
            segment = line.split(":")
            train = segment[3]
            clean_train = ""

            for s in train:
                if not s.isdigit():
                    clean_train += s
                else:
                    break

            if clean_train.strip() not in trains:
                trains.append(clean_train.strip())

    # sort trains
    trains.sort()

    for train in trains:

        count = 0

        output.append("")
        output.append(train)

        for line in data:

            if "rdar://" in line:
                if "confidential" in line:
                    hello = "1"

                else:
                    segment = line.split(":")[3]
                    if train in segment:
                        count += 1
                        total_count += 1
                        output.append(line)

        output[-count - 1] += " <{}>".format(count)

    for line in output:
        print(line)

    print("")
    print("Total bugs: " + str(total_count))


main()

# Find train: between second and third colon, and then before a number
# Add train to an array if the train does not exist in the array already
# now the array has all the trains
# sort it by ascending letters

# loop through the train array
# count = 0
# copy the train into a new array plus <>
# if item in array is found in data
# add to the array, count += 1
# put the count into the <> string

# done
