import unreal

def create_widget_blueprint(parent_class, widget_name, package_path):
    """Create a new Widget Blueprint."""
    factory = unreal.WidgetBlueprintFactory()
    factory.set_editor_property('ParentClass', parent_class)
    asset_tools = unreal.AssetToolsHelpers.get_asset_tools()
    return asset_tools.create_asset(widget_name, package_path, unreal.WidgetBlueprint, factory)

def add_widget_to_viewport(widget_class, z_order=0):
    """Add a widget to the viewport."""
    game_instance = unreal.get_editor_subsystem(unreal.EditorUtilitySubsystem)
    return game_instance.create_widget(widget_class, z_order)

def create_button(widget, button_name, text="Button", x=0, y=0):
    """Create a button in a widget."""
    if isinstance(widget, unreal.WidgetBlueprint):
        button = widget.add_new_widget(unreal.Button)
        button.set_editor_property('WidgetName', button_name)
        button.set_editor_property('Text', text)
        button.set_editor_property('Position', unreal.Vector2D(x, y))
        return button
    return None

def create_text_block(widget, text_name, text="Text", x=0, y=0):
    """Create a text block in a widget."""
    if isinstance(widget, unreal.WidgetBlueprint):
        text_block = widget.add_new_widget(unreal.TextBlock)
        text_block.set_editor_property('WidgetName', text_name)
        text_block.set_editor_property('Text', text)
        text_block.set_editor_property('Position', unreal.Vector2D(x, y))
        return text_block
    return None

def create_image(widget, image_name, image_path, x=0, y=0):
    """Create an image in a widget."""
    if isinstance(widget, unreal.WidgetBlueprint):
        image = widget.add_new_widget(unreal.Image)
        image.set_editor_property('WidgetName', image_name)
        image.set_editor_property('Brush', unreal.SlateBrush(image_path))
        image.set_editor_property('Position', unreal.Vector2D(x, y))
        return image
    return None

def set_widget_anchors(widget, min_x=0, min_y=0, max_x=1, max_y=1):
    """Set the anchors for a widget."""
    if widget:
        widget.set_editor_property('Anchors', unreal.Anchors(min_x, min_y, max_x, max_y))

def set_widget_alignment(widget, horizontal=0.5, vertical=0.5):
    """Set the alignment for a widget."""
    if widget:
        widget.set_editor_property('Alignment', unreal.Vector2D(horizontal, vertical))

def create_widget_binding(widget, property_name, binding_type):
    """Create a binding for a widget property."""
    if widget:
        return widget.add_binding(property_name, binding_type)

def create_widget_animation(widget, animation_name, length=1.0):
    """Create an animation for a widget."""
    if isinstance(widget, unreal.WidgetBlueprint):
        return widget.add_new_animation(animation_name, length)
    return None

def add_animation_track(animation, track_name, property_path):
    """Add a track to a widget animation."""
    if animation:
        return animation.add_track(track_name, property_path)
    return None 