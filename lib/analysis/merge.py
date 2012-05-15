import json


combined_data = {}

def combine(files, directory):
    global combined_data
    length = len(files)

    combined_data = {
        'num_files' : length
    }

    for json_file in files:
        f = open(directory + json_file, 'r')
        data = json.loads(f.read())
        process_package(data)
        f.close()

    f = open(directory + '../combined.json', 'w')
    f.write(json.dumps(combined_data))
    f.close()

def process_package(data):
    global combined_data
    packages = {}

    for key,value in data.iteritems():
        if key not in combined_data:
            combined_data[key] = {}
        process_class(key, value)

def process_class(package_name, data):
    global combined_data

    for key,value in data.iteritems():
        if key not in combined_data[package_name]:
            combined_data[package_name][key] = {}

        process_method(package_name, key, value)

def process_method(package_name, class_name, data):
    global combined_data

    for key,value in data.iteritems():
        if key not in combined_data[package_name][class_name]:
            combined_data[package_name][class_name][key] = 0

        covered = value['counters']['METHOD']['covered']

        if covered == "1":
            combined_data[package_name][class_name][key] += 1
