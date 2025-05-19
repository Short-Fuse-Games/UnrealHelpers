import unreal

def create_animation_sequence(skeleton, sequence_name, package_path):
    """Create a new animation sequence."""
    factory = unreal.AnimationSequenceFactory()
    factory.set_editor_property('TargetSkeleton', skeleton)
    asset_tools = unreal.AssetToolsHelpers.get_asset_tools()
    return asset_tools.create_asset(sequence_name, package_path, unreal.AnimationSequence, factory)

def add_animation_notify(sequence, notify_class, time, notify_name):
    """Add an animation notify to a sequence."""
    if isinstance(sequence, unreal.AnimationSequence):
        notify = sequence.add_notify(notify_class, time)
        notify.set_editor_property('NotifyName', notify_name)
        return notify
    return None

def create_animation_montage(skeleton, montage_name, package_path):
    """Create a new animation montage."""
    factory = unreal.AnimationMontageFactory()
    factory.set_editor_property('TargetSkeleton', skeleton)
    asset_tools = unreal.AssetToolsHelpers.get_asset_tools()
    return asset_tools.create_asset(montage_name, package_path, unreal.AnimationMontage, factory)

def add_section_to_montage(montage, section_name, start_time, end_time):
    """Add a section to an animation montage."""
    if isinstance(montage, unreal.AnimationMontage):
        return montage.add_section(section_name, start_time, end_time)
    return None

def create_animation_blendspace(skeleton, blendspace_name, package_path):
    """Create a new animation blendspace."""
    factory = unreal.BlendSpaceFactory1D()
    factory.set_editor_property('TargetSkeleton', skeleton)
    asset_tools = unreal.AssetToolsHelpers.get_asset_tools()
    return asset_tools.create_asset(blendspace_name, package_path, unreal.BlendSpace1D, factory)

def add_animation_to_blendspace(blendspace, animation, position):
    """Add an animation to a blendspace."""
    if isinstance(blendspace, unreal.BlendSpace1D):
        return blendspace.add_animation(animation, position)
    return None

def create_animation_state_machine(skeleton, state_machine_name, package_path):
    """Create a new animation state machine."""
    factory = unreal.AnimationStateMachineFactory()
    factory.set_editor_property('TargetSkeleton', skeleton)
    asset_tools = unreal.AssetToolsHelpers.get_asset_tools()
    return asset_tools.create_asset(state_machine_name, package_path, unreal.AnimationStateMachine, factory)

def add_state_to_state_machine(state_machine, state_name, animation):
    """Add a state to an animation state machine."""
    if isinstance(state_machine, unreal.AnimationStateMachine):
        return state_machine.add_state(state_name, animation)
    return None

def add_transition_to_state_machine(state_machine, from_state, to_state, transition_name):
    """Add a transition between states in a state machine."""
    if isinstance(state_machine, unreal.AnimationStateMachine):
        return state_machine.add_transition(from_state, to_state, transition_name)
    return None

def set_animation_sequence_length(sequence, length):
    """Set the length of an animation sequence."""
    if isinstance(sequence, unreal.AnimationSequence):
        sequence.set_editor_property('SequenceLength', length)

def set_animation_sequence_rate(sequence, rate):
    """Set the frame rate of an animation sequence."""
    if isinstance(sequence, unreal.AnimationSequence):
        sequence.set_editor_property('FrameRate', rate) 