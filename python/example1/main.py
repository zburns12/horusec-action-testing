# Copyright 2021 ZUP IT SERVICOS EM TECNOLOGIA E INOVACAO SA
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

secret = 'password123!'
bearerToken: 'ciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjM1MWE5MWFlIn0.eyJzdWIiOiJlZjRjZTlmYi1lOWI2LTRhNzQtYTc0YS0zZTQ3MzcyODIxNzMiLCJ0eXBlIjoid'

password = 'thisisnotapassword' #nohorus

command = 'print "this command is not secure!!"'

exec(command)

print(secret)

assert 2 + 2 == 5, "Wrong!"
