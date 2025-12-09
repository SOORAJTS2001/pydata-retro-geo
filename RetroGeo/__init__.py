import asyncio
import csv
import os
from io import StringIO

import httpx
import pandas as pd
from aiocache import cached
from aiocache.serializers import PickleSerializer

from RetroGeo.thread_type import ProcessTypeEnum
from RetroGeo.retro_geo import search


class GeoLocator:
    def __init__(self):
        self.countries = {}
        self.states = {}
    def query(self, locations: list,
              mode: ProcessTypeEnum = ProcessTypeEnum.MULTI_PROCESS.value):
        return search(locations, mode=mode)
