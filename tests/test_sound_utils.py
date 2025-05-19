import unittest
import unreal
from sound_utils import *
from tests.test_config import *

class TestSoundUtils(unittest.TestCase):
    def setUp(self):
        """Set up test environment before each test."""
        self.test_package_path = TEST_SOUND_PATH
        self.test_sound_name = TEST_SOUND_NAME
        self.test_sound_file = "/Game/Test/Sounds/test_sound.wav"  # You'll need to provide a test sound file

    def test_create_sound_wave(self):
        """Test sound wave creation."""
        sound_wave = create_sound_wave(
            self.test_sound_name,
            self.test_package_path,
            self.test_sound_file
        )
        self.assertIsNotNone(sound_wave)
        self.assertIsInstance(sound_wave, unreal.SoundWave)

    def test_create_sound_cue(self):
        """Test sound cue creation."""
        sound_cue = create_sound_cue(
            self.test_sound_name,
            self.test_package_path
        )
        self.assertIsNotNone(sound_cue)
        self.assertIsInstance(sound_cue, unreal.SoundCue)

    def test_add_sound_to_cue(self):
        """Test adding sound to cue."""
        sound_wave = create_sound_wave(
            "TestWave",
            self.test_package_path,
            self.test_sound_file
        )
        sound_cue = create_sound_cue(
            self.test_sound_name,
            self.test_package_path
        )
        result = add_sound_to_cue(sound_cue, sound_wave)
        self.assertIsNotNone(result)
        self.assertTrue(result)

    def test_create_sound_mix(self):
        """Test sound mix creation."""
        sound_mix = create_sound_mix(
            "TestMix",
            self.test_package_path
        )
        self.assertIsNotNone(sound_mix)
        self.assertIsInstance(sound_mix, unreal.SoundMix)

    def test_add_effect_to_sound_mix(self):
        """Test adding effect to sound mix."""
        sound_mix = create_sound_mix(
            "TestMix",
            self.test_package_path
        )
        effect = add_effect_to_sound_mix(
            sound_mix,
            unreal.SoundEffectSourcePreset,
            "TestEffect"
        )
        self.assertIsNotNone(effect)
        self.assertEqual(effect.get_editor_property('EffectName'), "TestEffect")

    def test_create_sound_class(self):
        """Test sound class creation."""
        sound_class = create_sound_class(
            "TestClass",
            self.test_package_path
        )
        self.assertIsNotNone(sound_class)
        self.assertIsInstance(sound_class, unreal.SoundClass)

    def test_set_sound_class_properties(self):
        """Test setting sound class properties."""
        sound_class = create_sound_class(
            "TestClass",
            self.test_package_path
        )
        set_sound_class_properties(
            sound_class,
            volume=0.8,
            pitch=1.2,
            low_pass_filter_frequency=1000.0
        )
        self.assertEqual(sound_class.get_editor_property('Volume'), 0.8)
        self.assertEqual(sound_class.get_editor_property('Pitch'), 1.2)
        self.assertEqual(sound_class.get_editor_property('LowPassFilterFrequency'), 1000.0)

    def test_create_sound_attenuation(self):
        """Test sound attenuation creation."""
        attenuation = create_sound_attenuation(
            "TestAttenuation",
            self.test_package_path
        )
        self.assertIsNotNone(attenuation)
        self.assertIsInstance(attenuation, unreal.SoundAttenuation)

    def test_set_attenuation_properties(self):
        """Test setting attenuation properties."""
        attenuation = create_sound_attenuation(
            "TestAttenuation",
            self.test_package_path
        )
        set_attenuation_properties(
            attenuation,
            falloff_distance=2000.0,
            spatialization=True
        )
        self.assertEqual(attenuation.get_editor_property('FalloffDistance'), 2000.0)
        self.assertTrue(attenuation.get_editor_property('bSpatialize'))

    def tearDown(self):
        """Clean up after each test."""
        # Add cleanup code here if needed
        pass

if __name__ == '__main__':
    unittest.main() 