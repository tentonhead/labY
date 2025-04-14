def data(labels, file_name="input.csv"):
    """Reads data from file and parses it into Records."""
    data = read_data(file_name)
    records = parse_data(data, labels)
    return records


def read_data(file_name):
    """Stores file contents in array and returns it"""
    data = []
    with open(file_name, "r") as file:
            data = file.readlines()
    return data


def parse_data(data, labels):
    """Splits data into columns by ',' and converts them to numeric types."""
    entries = len(data[0].split(','))
    columns = [[] for i in range(entries)]
    for i in range(len(data)):
        try:
            line = data[i].split(',')
        except:
            print(f"line {i} skipped")
            continue
        else:
            for j in range(len(line)):
                num = line[j].strip()
                if '.' in num:
                        num = float(num)
                elif 'j' in num:
                    num = complex(num)
                else:
                    num = int(num)
                columns[j].append(num)
    records = []
    for i in range(len(labels)):
        records.append(Record(np.array(columns[i]), labels[i]))
    return records
