import unreal

def create_blueprint(parent_class, blueprint_name, package_path):
    """Create a new Blueprint from a parent class."""
    factory = unreal.BlueprintFactory()
    factory.set_editor_property('ParentClass', parent_class)
    asset_tools = unreal.AssetToolsHelpers.get_asset_tools()
    return asset_tools.create_asset(blueprint_name, package_path, unreal.Blueprint, factory)

def add_variable_to_blueprint(blueprint, var_name, var_type, default_value=None, category="Default", tooltip=""):
    """Add a new variable to a Blueprint with additional properties."""
    if isinstance(blueprint, unreal.Blueprint):
        new_var = blueprint.add_new_variable(var_name, var_type)
        if default_value is not None:
            new_var.set_editor_property('DefaultValue', default_value)
        new_var.set_editor_property('Category', category)
        new_var.set_editor_property('ToolTip', tooltip)
        return new_var
    return None

def add_function_to_blueprint(blueprint, function_name, is_pure=False, is_const=False):
    """Add a new function to a Blueprint with additional properties."""
    if isinstance(blueprint, unreal.Blueprint):
        new_function = blueprint.add_new_function(function_name)
        new_function.set_editor_property('bIsPure', is_pure)
        new_function.set_editor_property('bIsConst', is_const)
        return new_function
    return None

def add_event_to_blueprint(blueprint, event_name):
    """Add a new event to a Blueprint."""
    if isinstance(blueprint, unreal.Blueprint):
        return blueprint.add_new_event(event_name)
    return None

def add_begin_play_event(blueprint):
    """Add a BeginPlay event to the Blueprint."""
    if isinstance(blueprint, unreal.Blueprint):
        return blueprint.add_new_event('ReceiveBeginPlay')
    return None

def add_tick_event(blueprint):
    """Add a Tick event to the Blueprint."""
    if isinstance(blueprint, unreal.Blueprint):
        return blueprint.add_new_event('ReceiveTick')
    return None

def add_node_to_function(function, node_class, x=0, y=0):
    """Add a new node to a function graph."""
    if function and hasattr(function, 'graph'):
        return function.graph.add_node(node_class, x, y)
    return None

def connect_nodes(from_node, to_node, from_pin_name="", to_pin_name=""):
    """Connect two nodes in the graph."""
    if from_node and to_node:
        from_pin = from_node.find_pin(from_pin_name) if from_pin_name else from_node.get_pin_at_index(0)
        to_pin = to_node.find_pin(to_pin_name) if to_pin_name else to_node.get_pin_at_index(0)
        if from_pin and to_pin:
            from_pin.make_link_to(to_pin)

def add_variable_get_node(function, variable_name, x=0, y=0):
    """Add a variable get node to a function."""
    if function and hasattr(function, 'graph'):
        return function.graph.add_node(unreal.K2Node_VariableGet, x, y, variable_name)
    return None

def add_variable_set_node(function, variable_name, x=0, y=0):
    """Add a variable set node to a function."""
    if function and hasattr(function, 'graph'):
        return function.graph.add_node(unreal.K2Node_VariableSet, x, y, variable_name)
    return None

def add_if_node(function, x=0, y=0):
    """Add an if/else node to a function."""
    if function and hasattr(function, 'graph'):
        return function.graph.add_node(unreal.K2Node_If, x, y)
    return None

def add_for_loop_node(function, x=0, y=0):
    """Add a for loop node to a function."""
    if function and hasattr(function, 'graph'):
        return function.graph.add_node(unreal.K2Node_ForLoop, x, y)
    return None

def add_math_node(function, operation_type, x=0, y=0):
    """Add a math operation node to a function."""
    if function and hasattr(function, 'graph'):
        return function.graph.add_node(unreal.K2Node_CallFunction, x, y, operation_type)
    return None

def get_blueprint_variables(blueprint):
    """Get all variables from a Blueprint."""
    if isinstance(blueprint, unreal.Blueprint):
        return blueprint.get_editor_property('NewVariables')
    return []

def get_blueprint_functions(blueprint):
    """Get all functions from a Blueprint."""
    if isinstance(blueprint, unreal.Blueprint):
        return blueprint.get_editor_property('FunctionGraphs')
    return []

def get_blueprint_events(blueprint):
    """Get all events from a Blueprint."""
    if isinstance(blueprint, unreal.Blueprint):
        return blueprint.get_editor_property('EventGraphs')
    return []

def set_variable_replication(blueprint, variable_name, replication_type):
    """Set the replication type for a variable."""
    if isinstance(blueprint, unreal.Blueprint):
        variables = get_blueprint_variables(blueprint)
        for var in variables:
            if var.get_name() == variable_name:
                var.set_editor_property('ReplicationType', replication_type)
                return True
    return False 