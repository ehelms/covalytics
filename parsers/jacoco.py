import xml.dom.minidom

def analyze(xml_data):
    parsed_data = parse_xml(xml_data)
    extracted_data = extract_method_data(parsed_data)
    extracted_data = extract_line_data(parsed_data, extracted_data)
    return extracted_data

def parse_xml(xml_data):
    return xml.dom.minidom.parse(xml_data)

def extract_method_data(dom):
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

def extract_line_data(dom, extracted_data):

    for node in dom.getElementsByTagName("package"):
        package_name = node.attributes['name'].childNodes[0].data.replace('/', '.')

        for child in node.childNodes:
            if child.nodeName == 'sourcefile':
                sourcefile_name = child.attributes['name'].childNodes[0].data.split('/').pop().split('.')[0]
                extracted_data[package_name][sourcefile_name]['lines'] = {}
                extracted_data[package_name][sourcefile_name]['counters'] = {}
                
                for item in child.childNodes:
                    if item.nodeName == 'line':
                        line_number = item.attributes['nr'].childNodes[0].data
                        missed_instructions = item.attributes['mi'].childNodes[0].data
                        covered_instructions = item.attributes['ci'].childNodes[0].data
                        missed_branches = item.attributes['mb'].childNodes[0].data
                        covered_branches = item.attributes['cb'].childNodes[0].data
                        
                        extracted_data[package_name][sourcefile_name]['lines'][line_number] = {
                            'missed_instructions'   : missed_instructions,
                            'covered_instructions'  : covered_instructions,
                            'missed_branches'       : missed_branches,
                            'covered_branches'      : covered_branches
                        }
                    elif item.nodeName == 'counter':
                        type    = item.attributes['type'].childNodes[0].data
                        missed  = item.attributes['missed'].childNodes[0].data
                        covered = item.attributes['covered'].childNodes[0].data

                        extracted_data[package_name][sourcefile_name]['counters'][type] = {
                            'missed'   : missed,
                            'covered'  : covered
                        }

    return extracted_data
