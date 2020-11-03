import pygame
import sys
import random
import os
import math
import time
import random
from main import *
from skull import *
from ball import *
from constant import *
from game import *
from player import *


class MainTest(unittest.TestCase):

    def test_make_Sprites(self):
    	text = "gj"
    	result = make_Sprites(0, 10, 10, "common", "Нулевой", 0, 45)
    	self.assertEqual(result, text)