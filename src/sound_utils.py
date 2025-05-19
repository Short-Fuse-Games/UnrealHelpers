import unreal

def create_sound_wave(sound_name, package_path, sound_file_path):
    """Create a new sound wave asset from a sound file."""
    factory = unreal.SoundWaveFactory()
    factory.set_editor_property('SoundFile', sound_file_path)
    asset_tools = unreal.AssetToolsHelpers.get_asset_tools()
    return asset_tools.create_asset(sound_name, package_path, unreal.SoundWave, factory)

def create_sound_cue(sound_name, package_path):
    """Create a new sound cue."""
    factory = unreal.SoundCueFactory()
    asset_tools = unreal.AssetToolsHelpers.get_asset_tools()
    return asset_tools.create_asset(sound_name, package_path, unreal.SoundCue, factory)

def add_sound_to_cue(sound_cue, sound_wave):
    """Add a sound wave to a sound cue."""
    if isinstance(sound_cue, unreal.SoundCue):
        return sound_cue.add_sound(sound_wave)
    return None

def create_sound_mix(sound_name, package_path):
    """Create a new sound mix."""
    factory = unreal.SoundMixFactory()
    asset_tools = unreal.AssetToolsHelpers.get_asset_tools()
    return asset_tools.create_asset(sound_name, package_path, unreal.SoundMix, factory)

def add_effect_to_sound_mix(sound_mix, effect_class, effect_name):
    """Add an effect to a sound mix."""
    if isinstance(sound_mix, unreal.SoundMix):
        effect = sound_mix.add_effect(effect_class)
        effect.set_editor_property('EffectName', effect_name)
        return effect
    return None

def create_sound_class(sound_name, package_path):
    """Create a new sound class."""
    factory = unreal.SoundClassFactory()
    asset_tools = unreal.AssetToolsHelpers.get_asset_tools()
    return asset_tools.create_asset(sound_name, package_path, unreal.SoundClass, factory)

def set_sound_class_properties(sound_class, volume=1.0, pitch=1.0, low_pass_filter_frequency=0.0):
    """Set properties for a sound class."""
    if isinstance(sound_class, unreal.SoundClass):
        sound_class.set_editor_property('Volume', volume)
        sound_class.set_editor_property('Pitch', pitch)
        sound_class.set_editor_property('LowPassFilterFrequency', low_pass_filter_frequency)

def create_sound_attenuation(sound_name, package_path):
    """Create a new sound attenuation settings."""
    factory = unreal.SoundAttenuationFactory()
    asset_tools = unreal.AssetToolsHelpers.get_asset_tools()
    return asset_tools.create_asset(sound_name, package_path, unreal.SoundAttenuation, factory)

def set_attenuation_properties(attenuation, falloff_distance=1000.0, spatialization=True):
    """Set properties for sound attenuation."""
    if isinstance(attenuation, unreal.SoundAttenuation):
        attenuation.set_editor_property('FalloffDistance', falloff_distance)
        attenuation.set_editor_property('bSpatialize', spatialization)

def play_sound_at_location(world, sound, location, volume_multiplier=1.0, pitch_multiplier=1.0):
    """Play a sound at a specific location in the world."""
    if world and sound:
        return unreal.GameplayStatics.play_sound_at_location(
            world,
            sound,
            location,
            volume_multiplier=volume_multiplier,
            pitch_multiplier=pitch_multiplier
        )
    return None

def play_sound_2d(world, sound, volume_multiplier=1.0, pitch_multiplier=1.0):
    """Play a 2D sound (no spatialization)."""
    if world and sound:
        return unreal.GameplayStatics.play_sound_2d(
            world,
            sound,
            volume_multiplier=volume_multiplier,
            pitch_multiplier=pitch_multiplier
        )
    return None 