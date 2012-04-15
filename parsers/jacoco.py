import xml.dom.minidom

def analyze(xml_data):
    parsed_data = parse_xml(xml_data)
    extracted_data = extract_data(parsed_data)
    return extracted_data

def parse_xml(xml_data):
    return xml.dom.minidom.parse(xml_data)

def extract_data(dom):
    extracted_data = {}

    for node in dom.getElementsByTagName("package"):
        package_name = node.attributes['name'].childNodes[0].data.replace('/', '.')
        extracted_data[package_name] = {}

        for child in node.childNodes:
            if child.nodeName == 'class':
                class_name = child.attributes['name'].childNodes[0].data.split('/').pop()
                extracted_data[package_name][class_name] = {}
                
                for item in child.childNodes:
                    if item.nodeName == 'method':
                        method_name = item.attributes['name'].childNodes[0].data
                        extracted_data[package_name][class_name][method_name] = {}

                        extracted_data[package_name][class_name][method_name]['counters'] = {}
                        for counter in item.childNodes:
                            counter_name = counter.attributes['type'].childNodes[0].data
                            extracted_data[package_name][class_name][method_name]['counters'][counter_name] = {}
                            for elem in counter.attributes.items():
                                extracted_data[package_name][class_name][method_name]['counters'][counter_name][elem[0]] = elem[1]

    return extracted_data
