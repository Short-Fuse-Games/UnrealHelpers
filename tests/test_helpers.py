import unreal
import os
from tests.test_config import *

def create_test_directory(path):
    """Create a test directory if it doesn't exist."""
    if not unreal.EditorAssetLibrary.does_directory_exist(path):
        unreal.EditorAssetLibrary.make_directory(path)

def cleanup_test_assets(prefix=TEST_ASSET_PREFIX):
    """Clean up test assets with the given prefix."""
    if not CLEANUP_TEST_ASSETS:
        return

    # Get all assets in test directories
    test_paths = [
        TEST_WIDGET_PATH,
        TEST_ANIMATION_PATH,
        TEST_SOUND_PATH
    ]

    for path in test_paths:
        if unreal.EditorAssetLibrary.does_directory_exist(path):
            assets = unreal.EditorAssetLibrary.list_assets(path, recursive=True)
            for asset in assets:
                if os.path.basename(asset).startswith(prefix):
                    unreal.EditorAssetLibrary.delete_asset(asset)

def get_test_skeleton():
    """Get a reference to a test skeleton."""
    return unreal.EditorAssetLibrary.load_asset("/Game/Test/Mannequin/Mesh/SK_Mannequin")

def get_test_sound_file():
    """Get a reference to a test sound file."""
    return unreal.EditorAssetLibrary.load_asset(TEST_SOUND_FILE)

def create_test_world():
    """Create a test world for testing gameplay functionality."""
    world = unreal.EditorLevelLibrary.get_editor_world()
    if not world:
        world = unreal.EditorLevelLibrary.new_level("/Game/Test/Maps/TestMap")
    return world

def cleanup_test_world():
    """Clean up the test world."""
    world = unreal.EditorLevelLibrary.get_editor_world()
    if world:
        actors = unreal.EditorLevelLibrary.get_all_level_actors()
        for actor in actors:
            if actor.get_name().startswith(TEST_ASSET_PREFIX):
                unreal.EditorLevelLibrary.destroy_actor(actor)

def setup_test_environment():
    """Set up the test environment."""
    # Create test directories
    create_test_directory(TEST_PACKAGE_PATH)
    create_test_directory(TEST_WIDGET_PATH)
    create_test_directory(TEST_ANIMATION_PATH)
    create_test_directory(TEST_SOUND_PATH)

def teardown_test_environment():
    """Clean up the test environment."""
    if CLEANUP_TEST_ASSETS:
        cleanup_test_assets()
        cleanup_test_world() 