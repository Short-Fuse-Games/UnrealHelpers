import unreal

def create_material_instance(parent_material_path, instance_name, instance_path):
    """Create a material instance from a parent material."""
    asset_tools = unreal.AssetToolsHelpers.get_asset_tools()
    parent_material = unreal.EditorAssetLibrary.load_asset(parent_material_path)
    if parent_material:
        return asset_tools.create_asset(instance_name, instance_path, unreal.MaterialInstanceConstant, parent_material)
    return None

def set_material_parameter(material_instance, parameter_name, value):
    """Set a parameter value on a material instance."""
    if isinstance(material_instance, unreal.MaterialInstanceConstant):
        material_instance.set_editor_property(parameter_name, value)
        unreal.EditorAssetLibrary.save_asset(material_instance.get_path_name())

def get_material_parameters(material_instance):
    """Get all parameters from a material instance."""
    if isinstance(material_instance, unreal.MaterialInstanceConstant):
        return material_instance.get_editor_property('parameter_values')
    return []

def create_material_expression(material, expression_class, x=0, y=0):
    """Create a material expression in a material."""
    if isinstance(material, unreal.Material):
        expression = material.create_material_expression(expression_class)
        expression.set_editor_property('material_expression_editor_x', x)
        expression.set_editor_property('material_expression_editor_y', y)
        return expression
    return None

def connect_material_expressions(from_expression, to_expression, from_output=0, to_input=0):
    """Connect two material expressions."""
    if from_expression and to_expression:
        to_expression.connect_expression(from_expression, to_input, from_output) 