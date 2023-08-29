import javalang

def generate_constructor(class_name, fields):
    constructor_params = ", ".join([f"{field['type']} {field['name']}" for field in fields])
    constructor_body = "\n".join([f"this.{field['name']} = {field['name']};" for field in fields])
    constructor = f"public {class_name}({constructor_params}) {{\n{constructor_body}\n}}\n"
    return constructor

def generate_getters(class_name, fields):
    getters = []
    for field in fields:
        field_name = field['name']
        getter_name = f"get{field_name.capitalize()}"
        getter_type = field['type']
        getter = f"public {getter_type} {getter_name}() {{\nreturn {field_name};\n}}\n"
        getters.append(getter)
    return getters

def generate_setters(class_name, fields):
    setters = []
    for field in fields:
        field_name = field['name']
        setter_name = f"set{field_name.capitalize()}"
        setter_type = field['type']
        setter = f"public void {setter_name}({setter_type} {field_name}) {{\nthis.{field_name} = {field_name};\n}}\n"
        setters.append(setter)
    return setters

def generate_code(class_name, fields):
    constructor = generate_constructor(class_name, fields)
    getters = generate_getters(class_name, fields)
    setters = generate_setters(class_name, fields)
    generated_code = constructor + "\n".join(getters) + "\n" + "\n".join(setters)
    return generated_code

def parse_java_file(file_path):
    with open(file_path, "r",encoding='u8') as file:
        java_code = file.read()
    tree = javalang.parse.parse(java_code)
    for path, node in tree:
        if isinstance(node, javalang.tree.ClassDeclaration):
            class_name = node.name
            fields = []
            for field_declaration in node.fields:
                field_type = field_declaration.type.name
                field_name = field_declaration.declarators[0].name
                fields.append({"type": field_type, "name": field_name})
            generated_code = generate_code(class_name, fields)
            return generated_code

java_file_path = "User.java"
generated_code = parse_java_file(java_file_path)
print(generated_code)
