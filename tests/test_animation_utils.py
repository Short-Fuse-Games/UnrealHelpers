import unittest
import unreal
from animation_utils import *
from tests.test_config import *

class TestAnimationUtils(unittest.TestCase):
    def setUp(self):
        """Set up test environment before each test."""
        self.test_package_path = TEST_ANIMATION_PATH
        self.test_animation_name = TEST_ANIMATION_NAME
        # Get a reference to a test skeleton
        self.skeleton = unreal.EditorAssetLibrary.load_asset("/Game/Test/Mannequin/Mesh/SK_Mannequin")

    def test_create_animation_sequence(self):
        """Test animation sequence creation."""
        sequence = create_animation_sequence(
            self.skeleton,
            self.test_animation_name,
            self.test_package_path
        )
        self.assertIsNotNone(sequence)
        self.assertIsInstance(sequence, unreal.AnimationSequence)

    def test_add_animation_notify(self):
        """Test adding animation notify."""
        sequence = create_animation_sequence(
            self.skeleton,
            self.test_animation_name,
            self.test_package_path
        )
        notify = add_animation_notify(
            sequence,
            unreal.AnimNotify,
            1.0,
            "TestNotify"
        )
        self.assertIsNotNone(notify)
        self.assertEqual(notify.get_editor_property('NotifyName'), "TestNotify")

    def test_create_animation_montage(self):
        """Test animation montage creation."""
        montage = create_animation_montage(
            self.skeleton,
            "TestMontage",
            self.test_package_path
        )
        self.assertIsNotNone(montage)
        self.assertIsInstance(montage, unreal.AnimationMontage)

    def test_add_section_to_montage(self):
        """Test adding section to montage."""
        montage = create_animation_montage(
            self.skeleton,
            "TestMontage",
            self.test_package_path
        )
        section = add_section_to_montage(montage, "TestSection", 0.0, 1.0)
        self.assertIsNotNone(section)
        self.assertEqual(section.get_editor_property('StartTime'), 0.0)
        self.assertEqual(section.get_editor_property('EndTime'), 1.0)

    def test_create_animation_blendspace(self):
        """Test animation blendspace creation."""
        blendspace = create_animation_blendspace(
            self.skeleton,
            "TestBlendSpace",
            self.test_package_path
        )
        self.assertIsNotNone(blendspace)
        self.assertIsInstance(blendspace, unreal.BlendSpace1D)

    def test_animation_sequence_properties(self):
        """Test setting animation sequence properties."""
        sequence = create_animation_sequence(
            self.skeleton,
            self.test_animation_name,
            self.test_package_path
        )
        set_animation_sequence_length(sequence, 2.0)
        set_animation_sequence_rate(sequence, 30.0)
        
        self.assertEqual(sequence.get_editor_property('SequenceLength'), 2.0)
        self.assertEqual(sequence.get_editor_property('FrameRate'), 30.0)

    def tearDown(self):
        """Clean up after each test."""
        # Add cleanup code here if needed
        pass

if __name__ == '__main__':
    unittest.main() 