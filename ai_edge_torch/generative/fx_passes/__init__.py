# Copyright 2024 The AI Edge Torch Authors.
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
# ==============================================================================
from ai_edge_torch import fx_infra
from ai_edge_torch.fx_infra import CanonicalizePass
from ai_edge_torch.generative.fx_passes.remove_sdpa_zero_mask_pass import RemoveSDPACompositeZeroMaskPass
import torch


def run_generative_passes(
    exported_program: torch.export.ExportedProgram,
) -> torch.export.ExportedProgram:
  return fx_infra.run_passes(
      exported_program,
      [RemoveSDPACompositeZeroMaskPass()],
  )
