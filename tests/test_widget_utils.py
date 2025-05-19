import unittest
import unreal
from widget_utils import *
from tests.test_config import *

class TestWidgetUtils(unittest.TestCase):
    def setUp(self):
        """Set up test environment before each test."""
        self.test_package_path = TEST_WIDGET_PATH
        self.test_widget_name = TEST_WIDGET_NAME
        self.parent_class = getattr(unreal, TEST_PARENT_CLASSES['widget'])

    def test_create_widget_blueprint(self):
        """Test widget blueprint creation."""
        widget = create_widget_blueprint(
            self.parent_class,
            self.test_widget_name,
            self.test_package_path
        )
        self.assertIsNotNone(widget)
        self.assertIsInstance(widget, unreal.WidgetBlueprint)

    def test_create_button(self):
        """Test button creation in widget."""
        widget = create_widget_blueprint(
            self.parent_class,
            self.test_widget_name,
            self.test_package_path
        )
        button = create_button(
            widget,
            "TestButton",
            TEST_BUTTON_TEXT,
            *TEST_POSITION
        )
        self.assertIsNotNone(button)
        self.assertEqual(button.get_editor_property('Text'), TEST_BUTTON_TEXT)

    def test_create_text_block(self):
        """Test text block creation in widget."""
        widget = create_widget_blueprint(
            self.parent_class,
            self.test_widget_name,
            self.test_package_path
        )
        text = create_text_block(
            widget,
            "TestText",
            TEST_TEXT,
            *TEST_POSITION
        )
        self.assertIsNotNone(text)
        self.assertEqual(text.get_editor_property('Text'), TEST_TEXT)

    def test_widget_anchors(self):
        """Test widget anchor settings."""
        widget = create_widget_blueprint(
            self.parent_class,
            self.test_widget_name,
            self.test_package_path
        )
        button = create_button(widget, "TestButton", TEST_BUTTON_TEXT, 0, 0)
        set_widget_anchors(button, *TEST_ANCHORS)
        anchors = button.get_editor_property('Anchors')
        self.assertEqual(anchors.minimum.x, TEST_ANCHORS[0])
        self.assertEqual(anchors.minimum.y, TEST_ANCHORS[1])

    def test_widget_animation(self):
        """Test widget animation creation."""
        widget = create_widget_blueprint(
            self.parent_class,
            self.test_widget_name,
            self.test_package_path
        )
        animation = create_widget_animation(
            widget,
            "TestAnimation",
            TEST_ANIMATION_LENGTH
        )
        self.assertIsNotNone(animation)
        self.assertEqual(
            animation.get_editor_property('Length'),
            TEST_ANIMATION_LENGTH
        )

    def tearDown(self):
        """Clean up after each test."""
        # Add cleanup code here if needed
        pass

if __name__ == '__main__':
    unittest.main() 