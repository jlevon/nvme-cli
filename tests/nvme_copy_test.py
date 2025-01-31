# SPDX-License-Identifier: GPL-2.0-only
#
# This file is part of nvme-cli
#
# Copyright (c) 2022 Samsung Electronics Co., Ltd. All Rights Reserved.
#
# Author: Arunpandian J <apj.arun@samsung.com>

"""
NVMe Copy Testcase:-

    1. Issue copy command on set of block; shall pass.

"""

from nose.tools import assert_equal
from nvme_test import TestNVMe


class TestNVMeCopy(TestNVMe):

    """
    Represents NVMe Verify testcase.
        - Attributes:
              - start_block :   starting block of to verify operation.
              - range :         Range of blocks for DSM operation.
              - slbs :          64-bit addr of first block per range
              - test_log_dir :  directory for logs, temp files.
    """

    def __init__(self):
        """ Pre Section for TestNVMeCopy """
        TestNVMe.__init__(self)
        self.start_block = 0
        self.range = 1
        self.slbs = 1
        self.namespace = 1
        self.setup_log_dir(self.__class__.__name__)

    def __del__(self):
        """ Post Section for TestNVMeCopy """
        TestNVMe.__del__(self)

    def copy(self):
        """ Wrapper for nvme copy
            - Args:
                - None
            - Returns:
                - return code for nvme copy command.
        """
        copy_cmd = "nvme copy " + self.ctrl + \
                   " --namespace-id=" + str(self.namespace) + \
                   " --sdlba=" + str(self.start_block) + \
                   " --blocks=" + str(self.range) + \
                   " --slbs=" + str(self.range)
        return self.exec_cmd(copy_cmd)

    def test_copy(self):
        """ Testcase main """
        assert_equal(self.copy(), 0)
