# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyLoralib(PythonPackage):
	"""PyTorch implementation of low-rank adaptation (LoRA), a parameter-efficient approach to adapt a large pre-trained deep learning model which obtains performance on-par with full fine-tuning."""
	
	homepage = "https://github.com/microsoft/LoRA"
	pypi = "loralib/loralib-0.1.2-py3-none-any.whl" 

	version("0.1.0", sha256="fdce4d1b3634f30e74b1264265c4a690d7fe861e9a02dc2519210bfcb61e982c", expand=False, url="https://files.pythonhosted.org/packages/d5/38/64b3766b76660142aa22764920861e954ca371b425e7a5206415d908ed5f/loralib-0.1.0-py3-none-any.whl")
	version("0.1.1", sha256="d641322de153588a4592aa2535ac1fd820344dfa43cdc7dd8f11c0956b740d7c", expand=False, url="https://files.pythonhosted.org/packages/8e/f5/2f6b453c81984a77d261f3f2b94715c63bba46c7a8b0d37445bbe8e74353/loralib-0.1.1-py3-none-any.whl")
	version("0.1.2", sha256="e341c9a507b180f3b8e70914efef9f6b19d1aa3996dec546b180cfbd027059e9", expand=False, url="https://files.pythonhosted.org/packages/f1/e7/a4362bf791bca17d2d91e7c69483185ab03d5aa05dd10391eff2e179a685/loralib-0.1.2-py3-none-any.whl")

	depends_on("python@3.6:", type=("build", "run"))
