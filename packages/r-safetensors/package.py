# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSafetensors(RPackage):
	"""Safetensors File Format

	A file format for storing tensors that is secure (doesn't allow for 
    code execution), fast and simple to implement. 'safetensors' also enables cross 
    language and cross frameworks compatibility making it an ideal format for 
    storing machine learning model weights.
	"""
	
	homepage = "https://github.com/mlverse/safetensors"
	cran = "safetensors" 

	version("0.1.2", md5="7fb57eff72a1e44950acb323bb51d14d")

	depends_on("r-cli", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
