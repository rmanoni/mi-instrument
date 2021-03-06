# #!/usr/bin/env python
#
# """Integration test base class and utils"""
#
# from mock import patch
# import unittest
# import os
# from gevent import greenlet, spawn
#
#
# from mi.core.bootstrap import bootstrap_pyon, CFG
#
# from mi.core import bootstrap
# from mi.core.bootstrap import bootstrap_pyon, CFG
# from mi.core.log import log
#
#
#
# def pre_initialize_ion():
#     # Do necessary system initialization
#     # Make sure this happens only once
#     iadm = InterfaceAdmin(bootstrap.get_sys_name(), config=CFG)
#     iadm.create_core_datastores()
#     iadm.store_interfaces(idempotent=True)
#     iadm.close()
#
# # This is the only place where code is executed once before any integration test
# # is run.
# def initialize_ion_int_tests():
#     # Bootstrap pyon CFG, logging and object/resource interfaces
#     bootstrap_pyon()
#     if bootstrap.is_testing():
#         IonIntegrationTestCase._force_clean(False)
#         pre_initialize_ion()
#
#
#
# class IonIntegrationTestCase(unittest.TestCase):
#     """
#     Base test class to allow operations such as starting the container
#     TODO: Integrate with IonUnitTestCase
#     """
#
#     # @see
#     # http://www.saltycrane.com/blog/2012/07/how-prevent-nose-unittest-using-docstring-when-verbosity-2/
#     def shortDescription(self):
#         return None
#
#     # override __str__ and __repr__ behavior to show a copy-pastable nosetest name for ion tests
#     #  ion.module:TestClassName.test_function_name
#     def __repr__(self):
#         name = self.id()
#         name = name.split('.')
#         if name[0] not in ["ion", "pyon"]:
#             return "%s (%s)" % (name[-1], '.'.join(name[:-1]))
#         else:
#             return "%s ( %s )" % (name[-1], '.'.join(name[:-2]) + ":" + '.'.join(name[-2:]))
#     __str__ = __repr__
#
#
#     def run(self, result=None):
#         unittest.TestCase.run(self, result)
#
#
#     def _start_tracer_log(self, config=None):
#         """Temporarily enables tracer log and configures it until end of test (cleanUp)"""
#         if not self.container:
#             return
#
#         if not tracer.trace_data["config"].get("log_trace", False):
#             tracer_cfg_old = tracer.trace_data["config"]
#             tracer.trace_data["config"] = tracer.trace_data["config"].copy()
#             tracer.trace_data["config"]["log_trace"] = True
#             if config:
#                 tracer.trace_data["config"].update(config)
#
#             def cleanup_tracer():
#                 tracer.trace_data["config"] = tracer_cfg_old
#                 log.info("--------------- Stopping Tracer Logging ---------------")
#             self.addCleanup(cleanup_tracer)
#             log.info("--------------- Starting Tracer Logging ---------------")
#
#     def _breakpoint(self, scope=None, global_scope=None):
#         from pyon.util.breakpoint import breakpoint
#         breakpoint(scope=scope, global_scope=global_scope)
#
#     def _turn_on_queue_auto_delete(self):
#         patcher = patch('pyon.net.channel.RecvChannel._queue_auto_delete', True)
#         patcher.start()
#         self.addCleanup(patcher.stop)
#
#     def _patch_out_diediedie(self):
#         """
#         If things are running slowly, diediedie will send a kill -9 to the owning process,
#         which could be the test runner! Let the test runner decide if it's time to die.
#         """
#         patcher = patch('pyon.core.thread.shutdown_or_die')
#         patcher.start()
#         self.addCleanup(patcher.stop)
#
#     def _patch_out_start_rel(self):
#         def start_rel_from_url(*args, **kwargs):
#             return True
#
#         patcher = patch('pyon.container.apps.AppManager.start_rel_from_url', start_rel_from_url)
#         patcher.start()
#         self.addCleanup(patcher.stop)
#
#     def _patch_out_fail_fast_kill(self):
#         # Not only is this an enormous hack, it doens't work :/
#         # reinvestigate later
#
#         patcher = patch('pyon.container.cc.Container._kill_fast')
#         patcher.start()
#         self.addCleanup(patcher.stop)
#
#     @classmethod
#     def _force_clean(cls, recreate=False):
#         from pyon.core.bootstrap import get_sys_name, CFG
#         from pyon.datastore.datastore_common import DatastoreFactory
#         datastore = DatastoreFactory.get_datastore(config=CFG, variant=DatastoreFactory.DS_BASE, scope=get_sys_name())
#         #datastore = DatastoreFactory.get_datastore(config=CFG, variant=DatastoreFactory.DS_BASE)
#
#         dbs = datastore.list_datastores()
#         things_to_clean = filter(lambda x: x.startswith('%s_' % get_sys_name().lower()), dbs)
#         try:
#             for thing in things_to_clean:
#                 datastore.delete_datastore(datastore_name=thing)
#                 if recreate:
#                     datastore.create_datastore(datastore_name=thing)
#
#         finally:
#             datastore.close()
#
#         if os.environ.get('CEI_LAUNCH_TEST', None) is None:
#             FileSystem._clean(CFG)
#
#
#     def patch_cfg(self, cfg_obj_or_str, *args, **kwargs):
#         """
#         Helper method for patching the CFG (or any dict, but useful for patching CFG).
#
#         This method exists because the decorator versions of patch/patch.dict do not function
#         until the test_ method is called - ie, when setUp is run, the patch hasn't occured yet.
#         Use this in your setUp method if you need to patch CFG and have stuff in setUp respect it.
#
#         @param  cfg_obj_or_str  An actual ref to CFG or a string defining where to find it ie 'pyon.ion.exchange.CFG'
#         @param  *args           *args to pass to patch.dict
#         @param  **kwargs        **kwargs to pass to patch.dict
#         """
#         patcher = patch.dict(cfg_obj_or_str, *args, **kwargs)
#         patcher.start()
#         self.addCleanup(patcher.stop)
#
# initialize_ion_int_tests()