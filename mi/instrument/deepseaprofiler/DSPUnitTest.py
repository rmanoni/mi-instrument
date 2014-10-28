#!/usr/bin/env python
# coding=utf-8
__author__ = 'rachelmanoni'

#$ bin/nosetests -s -v /Users/rachelmanoni/WorkSpace/mi-instrument/mi/instrument/deepseaprofiler -a UNIT

import json
import sys
sys.path.append('/Users/rachelmanoni/Workspace/mi-dataset/')

from nose.plugins.attrib import attr

from mi.core.log import get_logger
log = get_logger()

from mi.idk.unit_test import InstrumentDriverUnitTestCase, InstrumentDriverTestCase

from mi.instrument.deepseaprofiler.DeepSeaProfiler import Optode_L0_Particle, DATA_KEY, DataParticleType, \
    Acm_L0_Particle, Flcrtd_L0_Particle, Flnturtd_L0_Particle, Ctd_L1_Particle

InstrumentDriverTestCase.initialize(
    driver_module='mi.instrument.deepseaprofiler.DeepSeaProfiler',
    driver_class="",

    instrument_agent_resource_id='3DLE2A',
    instrument_agent_name='deepseaprofiler',
    instrument_agent_packet_config=DataParticleType(),

    driver_startup_config={}
)


@attr('UNIT', group='mi')
class DriverUnitTest(InstrumentDriverUnitTestCase):
    def setUp(self):
        InstrumentDriverUnitTestCase.setUp(self)

    def test_acm(self):

        raw_data = '{"data": {"hz": -0.9217000007629395, "va": 5.699999809265137, "vb": -3.7899999618530273, ' \
                   '"vc": -0.3499999940395355, "vd": -3.9100000858306885, "tx": -1.5199999809265137, ' \
                   '"ty": 0.3100000023841858, "hx": -0.3815000057220459, "hy": -0.07029999792575836}, ' \
                   '"name": "acm", "t": [1386089504, 777887]}'
        data_particle = json.loads(raw_data)
        particle = Acm_L0_Particle(data_particle[DATA_KEY])
        particle.generate()

    def test_ctd(self):
        raw_data = '{"data": {"condwat": 32.74679946899414, "tempwat": 8.356900215148926, ' \
                   '"preswat": 30.84000015258789}, "name": "ctd", "t": [1386089503, 508733]}'
        data_particle = json.loads(raw_data)
        particle = Ctd_L1_Particle(data_particle[DATA_KEY])
        particle.generate()

    def test_flcrtd(self):
        raw_data = '{"data": {"cdomflo": 187}, "name": "flcd", "t": [1386089504, 477380]}'
        data_particle = json.loads(raw_data)
        particle = Flcrtd_L0_Particle(data_particle[DATA_KEY])
        particle.generate()

    def test_flnturtd(self):
        raw_data = '{"data": {"ntuflo": 223, "chlaflo": 85}, "name": "flntu", "t": [1386089504, 417989]}'
        data_particle = json.loads(raw_data)
        particle = Flnturtd_L0_Particle(data_particle[DATA_KEY])
        particle.generate()

    def test_optode(self):
        raw_data = '{"data": {"doconcs": 38.07099914550781, "t": 8.383999824523926}, "name": "optode", ' \
                   '"t": [1386089504, 193578]}'
        data_particle = json.loads(raw_data)
        particle = Optode_L0_Particle(data_particle[DATA_KEY])
        particle.generate()

    def test_acs(self):
        #TODO
        pass




