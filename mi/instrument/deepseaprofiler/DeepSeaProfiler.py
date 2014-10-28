#!/usr/bin/env python
# coding=utf-8


__author__ = 'Rachel Manoni'
__license__ = 'Apache 2.0'

import json
import ntplib

from mi.core.log import get_logger
log = get_logger()

from mi.core.common import BaseEnum

from mi.core.exceptions import SampleException

from mi.core.instrument.data_particle import DataParticle
from mi.core.instrument.data_particle import DataParticleKey

#TODO - CANNT IMPORT!!!!!
#from mi.dataset.parser.optaa_ac_mmp_cds import OptaaAcMmpCdsParserDataParticle


TIMESTAMP_KEY = 't'
NAME_KEY = 'name'
DATA_KEY = 'data'


class DataParticleType(BaseEnum):
    CTD_L1 = 'ctd_l1'
    ACS_RAW = 'acs_raw'
    FLNTURTD_L0 = 'flnturtd_l0'
    FLCDRTD_L0 = 'flcrtd_l0'
    ACM_L0 = 'acm_l0'
    OPTODE_L0 = 'optode_l0'


class Ctd_L1_ParticleKey(BaseEnum):
    CONDWAT = 'condwat'
    TEMPWAT = 'tempwat'
    PRESWAT = 'preswat'


class Ctd_L1_Particle(DataParticle):

    _data_particle_type = DataParticleType.CTD_L1

    def _build_parsed_values(self):

        log.debug("raw data = %r", self.raw_data)
        try:
            result = [{DataParticleKey.VALUE_ID: Ctd_L1_ParticleKey.CONDWAT, DataParticleKey.VALUE: self.raw_data[Ctd_L1_ParticleKey.CONDWAT]},
                      {DataParticleKey.VALUE_ID: Ctd_L1_ParticleKey.TEMPWAT, DataParticleKey.VALUE: self.raw_data[Ctd_L1_ParticleKey.TEMPWAT]},
                      {DataParticleKey.VALUE_ID: Ctd_L1_ParticleKey.PRESWAT, DataParticleKey.VALUE: self.raw_data[Ctd_L1_ParticleKey.PRESWAT]}]
            log.debug('parsed particle = %r', result)
            return result

        except Exception:
            raise SampleException('Error building Ctd_L1_Particle')


# class Acs_Raw_Particle(OptaaAcMmpCdsParserDataParticle):
#
#     _data_particle_type = DataParticleType.ACS_RAW
#
#     def _build_parsed_values(self):
#         return self._get_mmp_cds_subclass_particle_params(self.raw_data)


class Flnturtd_L0_ParticleKey(BaseEnum):
    CHLAFLO = 'chlaflo'
    NTUFLO = 'ntuflo'


class Flnturtd_L0_Particle(DataParticle):

    _data_particle_type = DataParticleType.FLNTURTD_L0

    def _build_parsed_values(self):

        log.debug("raw data = %r", self.raw_data)
        try:
            result = [{DataParticleKey.VALUE_ID: Flnturtd_L0_ParticleKey.CHLAFLO, DataParticleKey.VALUE: self.raw_data[Flnturtd_L0_ParticleKey.CHLAFLO]},
                      {DataParticleKey.VALUE_ID: Flnturtd_L0_ParticleKey.NTUFLO, DataParticleKey.VALUE: self.raw_data[Flnturtd_L0_ParticleKey.NTUFLO]}]
            log.debug('parsed particle = %r', result)
            return result

        except Exception:
            raise SampleException('Error building Flnturtd_L0_Particle')


class Flcrtd_L0_ParticleKey(BaseEnum):
    CDOMFLO = 'cdomflo'


class Flcrtd_L0_Particle(DataParticle):

    _data_particle_type = DataParticleType.FLCDRTD_L0

    def _build_parsed_values(self):

        log.debug("raw data = %r", self.raw_data)
        try:
            result = [{DataParticleKey.VALUE_ID: Flcrtd_L0_ParticleKey.CDOMFLO, DataParticleKey.VALUE: self.raw_data[Flcrtd_L0_ParticleKey.CDOMFLO]}]
            log.debug('parsed particle = %r', result)
            return result

        except Exception:
            raise SampleException('Error building Flcrtd_L0_Particle')


class Acm_L0_ParticleKey(BaseEnum):
    VA = 'va'
    VB = 'vb'
    VC = 'vc'
    VD = 'vd'
    HX = 'hx'
    HY = 'hy'
    HZ = 'hz'
    TX = 'tx'
    TY = 'ty'


class Acm_L0_Particle(DataParticle):

    _data_particle_type = DataParticleType.ACM_L0

    def _build_parsed_values(self):

        log.debug("raw data = %r", self.raw_data)
        try:
            result = [{DataParticleKey.VALUE_ID: Acm_L0_ParticleKey.VA, DataParticleKey.VALUE: self.raw_data[Acm_L0_ParticleKey.VA]},
                      {DataParticleKey.VALUE_ID: Acm_L0_ParticleKey.VB, DataParticleKey.VALUE: self.raw_data[Acm_L0_ParticleKey.VB]},
                      {DataParticleKey.VALUE_ID: Acm_L0_ParticleKey.VC, DataParticleKey.VALUE: self.raw_data[Acm_L0_ParticleKey.VC]},
                      {DataParticleKey.VALUE_ID: Acm_L0_ParticleKey.VD, DataParticleKey.VALUE: self.raw_data[Acm_L0_ParticleKey.VD]},
                      {DataParticleKey.VALUE_ID: Acm_L0_ParticleKey.HX, DataParticleKey.VALUE: self.raw_data[Acm_L0_ParticleKey.HX]},
                      {DataParticleKey.VALUE_ID: Acm_L0_ParticleKey.HY, DataParticleKey.VALUE: self.raw_data[Acm_L0_ParticleKey.HY]},
                      {DataParticleKey.VALUE_ID: Acm_L0_ParticleKey.HZ, DataParticleKey.VALUE: self.raw_data[Acm_L0_ParticleKey.HZ]},
                      {DataParticleKey.VALUE_ID: Acm_L0_ParticleKey.TX, DataParticleKey.VALUE: self.raw_data[Acm_L0_ParticleKey.TX]},
                      {DataParticleKey.VALUE_ID: Acm_L0_ParticleKey.TY, DataParticleKey.VALUE: self.raw_data[Acm_L0_ParticleKey.TY]}]

            log.debug('parsed particle = %r', result)
            return result

        except Exception:
            raise SampleException('Error building Acm_L0_Particle')


class Optode_L0_ParticleKey(BaseEnum):
    DOCONCS = 'doconcs'
    T = 't'


class Optode_L0_Particle(DataParticle):

    _data_particle_type = DataParticleType.OPTODE_L0

    def _build_parsed_values(self):

        log.warn("raw data = %r", self.raw_data)
        try:
            result = [{DataParticleKey.VALUE_ID: Optode_L0_ParticleKey.DOCONCS, DataParticleKey.VALUE: self.raw_data[Optode_L0_ParticleKey.DOCONCS]},
                      {DataParticleKey.VALUE_ID: Optode_L0_ParticleKey.T, DataParticleKey.VALUE: self.raw_data[Optode_L0_ParticleKey.T]}]

            log.debug('parsed particle = %r', result)
            return result

        except Exception:
            raise SampleException('Error building Optode_L0_Particle')


def parse_science_data(self):

    data_particle = json.loads(self.raw_data)

    particle_map = {
        'ctd': Ctd_L1_Particle,
        'optode': Optode_L0_Particle,
        #'ac_s': Acs_Raw_Particle,
        'acm': Acm_L0_Particle,
        'flntu': Flnturtd_L0_Particle,
        'flcd': Flcrtd_L0_Particle
    }

    raw_time = data_particle[TIMESTAMP_KEY]
    raw_time_seconds = raw_time[0]
    raw_time_microseconds = raw_time[1]
    ntp_timestamp = ntplib.system_to_ntp_time(raw_time_seconds + raw_time_microseconds / 1000000.0)

    particle = particle_map[data_particle[NAME_KEY]](data_particle[DATA_KEY], internal_timestamp=ntp_timestamp,
                                                 preferred_timestamp=DataParticleKey.INTERNAL_TIMESTAMP)
    return particle.generate()

def parse_file(self):
    pass

