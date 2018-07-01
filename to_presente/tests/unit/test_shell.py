# Copyright (2018) Universidade Federal de Campina Grande
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import unittest

from to_presente.shell import Shell, main


class TestShell(unittest.TestCase):

    def setUp(self):
        self.shell = Shell()

    def test_numbers_3_4(self):
        self.assertEqual(self.shell.multiply(3, 4), 12)

    def test_strings_a_3(self):
        self.assertEqual(self.shell.times_three('a'), 'aaa')

    def test_main(self):
        main()


if __name__ == '__main__':
    unittest.main()
