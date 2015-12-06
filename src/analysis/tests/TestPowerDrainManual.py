# Standard imports
import unittest
import json
#from main import tripManager
from pymongo import MongoClient
import logging
from datetime import datetime, timedelta

# Our imports
import analysis.power_drain_manual as ap

logging.basicConfig(level=logging.DEBUG)

class TestPowerDrainManual(unittest.TestCase):
  def setUp(self):
    pass

  def tearDown(self):
    pass

  def testToHour(self):
    self.assertEqual(ap.secs_to_hour(1), 1 / (60 * 60))
    self.assertEqual(ap.secs_to_hour(60), 1 / 60)
    self.assertEqual(ap.secs_to_hour(3600), 1)

