import json
import xml.etree.ElementTree as etree


def connector_factory(file_path):
    '''factory method'''
    class JSONConnector:
        def __init__(self, file_path):
            self.data = {}
            with open(file_path, mode='r', encoding='utf-8') as f:
                self.data = json.load(f)

        @property
        def parse_data(self):
            return self.data

    class XMLConnector:
        def __init__(self, file_path):
            self.tree = etree.parse(file_path)

        @property
        def parse_data(self):
            return self.tree

    print("connector_factory is factory method.")
    if file_path.endswith('json'):
        print("create json connector")
        connector = JSONConnector
    elif file_path.endswith('xml'):
        print("create xml connector")
        connector = XMLConnector
    else:
        raise ValueError(f"Can not connect to {file_path}")
    return connector(file_path)


def connect_to(file_path):
    '''creator return a product'''
    product = None
    try:
        product = connector_factory(file_path)
    except ValueError as err:
        print(err)
    return product


def main():
    # sqlite_factory = connect_to()
    xml_product = connect_to('person.xml')
    xml_data = xml_product.parse_data
    liars = xml_data.findall(".//{}[{}='{}']".format('person', 'lastName', 'Liar'))
    print(f"found: {len(liars)} persons")
    for liar in liars:
        print(f"first name: {liar.find('firstName').text}")
        print(f"last name: {liar.find('lastName').text}")
        [print(f"phone number ({t.attrib['type']}): {t.text}") for t in liar.find('phoneNumbers')]

    json_product = connect_to('donut.json')
    json_data = json_product.parse_data
    print(f"found: {len(json_data)} donuts")
    for dount in json_data:
        print(f"name: {dount['name']}")
        print(f"price: ${dount['ppu']}")
        [print(f"topping: {t['id']} {t['type']}") for t in dount['topping']]


if __name__ == "__main__":
    main()
    
