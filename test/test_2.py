import unittest
import pytest
from unittest import TestCase
from ya_create_folder import create_folders

class TestYandex(TestCase):
    def test_create_folders(self):
        result = create_folders()
        expected = 201
        self.assertEqual(result, expected)
