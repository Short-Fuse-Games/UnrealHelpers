"""
Configuration settings for tests.
"""

# Test paths
TEST_PACKAGE_PATH = "/Game/Test"
TEST_WIDGET_PATH = f"{TEST_PACKAGE_PATH}/Widgets"
TEST_ANIMATION_PATH = f"{TEST_PACKAGE_PATH}/Animations"
TEST_SOUND_PATH = f"{TEST_PACKAGE_PATH}/Sounds"

# Test asset names
TEST_WIDGET_NAME = "TestWidget"
TEST_ANIMATION_NAME = "TestAnimation"
TEST_SOUND_NAME = "TestSound"

# Test data
TEST_TEXT = "Test Text"
TEST_BUTTON_TEXT = "Test Button"
TEST_POSITION = (100, 100)
TEST_ANCHORS = (0.5, 0.5, 0.5, 0.5)
TEST_ANIMATION_LENGTH = 2.0

# Sound test settings
TEST_SOUND_FILE = "/Game/Test/Sounds/test_sound.wav"
TEST_SOUND_VOLUME = 0.8
TEST_SOUND_PITCH = 1.2
TEST_SOUND_FILTER_FREQ = 1000.0
TEST_SOUND_FALLOFF = 2000.0

# Test classes
TEST_PARENT_CLASSES = {
    'widget': 'UserWidget',
    'animation': 'AnimInstance',
    'sound': 'SoundBase'
}

# Test cleanup settings
CLEANUP_TEST_ASSETS = True
TEST_ASSET_PREFIX = "Test_" 