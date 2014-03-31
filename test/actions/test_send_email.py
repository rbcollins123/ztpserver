#!/usr/bin/env python
#
# Copyright (c) 2014, Arista Networks, Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met:
#  - Redistributions of source code must retain the above copyright notice,
# this list of conditions and the following disclaimer.
#  - Redistributions in binary form must reproduce the above copyright
# notice, this list of conditions and the following disclaimer in the
# documentation and/or other materials provided with the distribution.
#  - Neither the name of Arista Networks nor the names of its
# contributors may be used to endorse or promote products derived from
# this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL ARISTA NETWORKS
# BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR
# BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY,
# WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE
# OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN
# IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

#pylint: disable=R0904,F0401,W0232,E1101

import os
import os.path
import unittest
import shutil
import sys

sys.path.append('test/client')

from client_test_lib import debug    #pylint: disable=W0611
from client_test_lib import Bootstrap, ActionFailureTest
from client_test_lib import file_log, get_action, random_string
from client_test_lib import startup_config_action, remove_file

class FailureTest(ActionFailureTest):

    def test_missing_smarthost(self):
        self.basic_test('send_email', 1)

    def test_missing_sender(self):
        self.basic_test('send_email', 2,
                        attributes={'smarthost' :
                                    random_string()})
    def test_missing_receivers(self):
        self.basic_test('send_email', 3,
                        attributes={'smarthost' :
                                    random_string(),
                                    'sender' :
                                    random_string()})


class SuccessTest(unittest.TestCase):
    pass


if __name__ == '__main__':
    unittest.main()