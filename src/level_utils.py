import unreal

def get_all_actors_in_level(level=None):
    """Get all actors in the current or specified level."""
    if level is None:
        level = unreal.EditorLevelLibrary.get_editor_world().get_current_level()
    return unreal.EditorLevelLibrary.get_all_level_actors(level)

def spawn_actor(actor_class, location, rotation=None):
    """Spawn an actor in the current level."""
    if rotation is None:
        rotation = unreal.Rotator(0, 0, 0)
    return unreal.EditorLevelLibrary.spawn_actor_from_class(actor_class, location, rotation)

def get_selected_actors():
    """Get all currently selected actors in the level."""
    return unreal.EditorLevelLibrary.get_selected_level_actors()

def delete_selected_actors():
    """Delete all selected actors in the level."""
    selected_actors = get_selected_actors()
    for actor in selected_actors:
        unreal.EditorLevelLibrary.destroy_actor(actor)

def get_actor_location(actor):
    """Get the location of an actor."""
    return actor.get_actor_location()

def set_actor_location(actor, location):
    """Set the location of an actor."""
    actor.set_actor_location(location, False, False) 