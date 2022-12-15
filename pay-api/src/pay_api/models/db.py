# Copyright © 2019 Province of British Columbia
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
"""Create SQLAlchemy and Schema managers.

These will get initialized by the application using the models
"""
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_continuum import make_versioned
from sqlalchemy_continuum.plugins import ActivityPlugin


# by convention in the Flask community these are lower case,
# whereas pylint wants them upper case
ma = Marshmallow()  # pylint: disable=invalid-name
db = SQLAlchemy()  # pylint: disable=invalid-name

activity_plugin = ActivityPlugin()  # pylint: disable=invalid-name

make_versioned(user_cls=None, plugins=[activity_plugin])
