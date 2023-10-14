def read_signal_text_file(path):
    file_contents = []
    with open(path, "r") as file:
        for line in file:
            file_contents.append(line.strip())

    return file_contents


def seperate_file_date(path):
    file_contents = read_signal_text_file(path)
    signal_type = int(file_contents[0])
    is_periodic =int(file_contents[1])
    n_samples = int(file_contents[2])
    data=[]
    for i in range(3, n_samples + 3):
        data.append([float(x) for x in file_contents[i].split()])
    return data, signal_type, is_periodic, n_samples