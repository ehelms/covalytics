import json

def generate(directory):
    f = open(directory + '/combined.json', 'r')
    data = json.loads(f.read())
    method_list = methods_by_most_hits(data)
    print_by_most_hits(method_list, data['num_files'])
    f.close()

def methods_by_most_hits(data):
    return_data = {}

    for package_name, classes in data.iteritems():
        if package_name != 'num_files':
            for class_name, methods in classes.iteritems():
                for method, count in methods.iteritems():
                    return_data[method] = count

    return return_data

def print_by_most_hits(data, num_files):
    for key, value in sorted(data.iteritems(), key=lambda (k,v): (v,k)):
        print "%s: \n %s %s%%" % (key, value, str((float(value) / float(num_files)) * 100))

def print_by_least_hits(data):
    for key, value in sorted(data.iteritems(), key=lambda (v,k): (k,v)):
        print "%s: %s" % (key, value)
