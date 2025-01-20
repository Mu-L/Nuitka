#     Copyright 2025, Kay Hayen, mailto:kay.hayen@gmail.com find license text at end of file


import itertools

module_value1 = 1000
module_value2 = 1000


def calledRepeatedly(cond):
    closure_value = module_value1

    def f():
        # Force frame and eliminate forward propagation (currently).
        module_value1

        local_value1 = module_value1
        local_value2 = module_value2

        if cond:
            local_value1 = closure_value

        return local_value1 + local_value2

    # Make it clear that the closure cannot be trusted and there
    # is no inlining possible.
    return f, f()


for x in itertools.repeat(None, 50000):
    # construct_begin
    calledRepeatedly(True)
    # construct_alternative
    calledRepeatedly(False)
    # construct_end

print("OK.")

#     Python test originally created or extracted from other peoples work. The
#     parts from me are licensed as below. It is at least Free Software where
#     it's copied from other people. In these cases, that will normally be
#     indicated.
#
#     Licensed under the Apache License, Version 2.0 (the "License");
#     you may not use this file except in compliance with the License.
#     You may obtain a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#     Unless required by applicable law or agreed to in writing, software
#     distributed under the License is distributed on an "AS IS" BASIS,
#     WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#     See the License for the specific language governing permissions and
#     limitations under the License.
