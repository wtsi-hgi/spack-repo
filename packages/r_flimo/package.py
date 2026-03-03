# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFlimo(RPackage):
	"""Fixed Landscape Inference Method

	Likelihood-free inference method for stochastic models.
    Uses a deterministic optimizer on simple simulations of the model
    that are performed with a prior drawn randomness by applying the inverse transform method.
    Is designed to work on its own and also by using the Julia package 'Jflimo'
    available on the git page of the project: <https://metabarcoding.org/flimo>.
	"""
	
	cran = "flimo" 

	version("0.1.5", md5="cc9804f87f5d64d16e5c5e9f3ed962d6")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-juliaconnector", type=("build", "run"))
