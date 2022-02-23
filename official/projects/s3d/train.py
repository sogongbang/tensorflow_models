# Copyright 2022 The TensorFlow Authors. All Rights Reserved.
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

# Lint as: python3
"""TensorFlow Model Garden Vision training driver for S3D."""

from absl import app

# pylint: disable=unused-import
from official.common import registry_imports
# pylint: enable=unused-import
from official.common import flags as tfm_flags
# pylint: disable=unused-import
from official.projects.s3d.configs.google import s3d as s3d_config
from official.projects.s3d.modeling import s3d
from official.projects.s3d.tasks.google import automl_video_classification
# pylint: enable=unused-import
from official.vision.beta import train

if __name__ == '__main__':
  tfm_flags.define_flags()
  app.run(train.main)