

def process_csv(csv_file):
    data = []

    if csv_file.content_type != 'text/csv':
        return data

    temp = ''
    for x, line in enumerate(csv_file):
        csv_data = line.decode('utf-8').strip()

        try:
            if csv_data == '':
                if temp:
                    data.append(temp)
                    temp = ''
            elif csv_data.startswith('"'):
                csv_data = csv_data[1:]
                temp = csv_data
            elif csv_data.endswith('"'):
                temp += csv_data[:-1]
                data.append(temp)
                temp = ''
            
            else:
                temp += csv_data
        except IndexError:
            print(f"Error processing line {x}: '{csv_data}'")

    if temp:
        data.append(temp)

    return data
