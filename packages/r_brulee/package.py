# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBrulee(RPackage):
	"""High-Level Modeling Functions with 'torch'

	Provides high-level modeling functions to define and train
    models using the 'torch' R package. Models include linear, logistic,
    and multinomial regression as well as multilayer perceptrons.
	"""
	
	homepage = "https://github.com/tidymodels/brulee"
	cran = "brulee" 

	version("0.3.0", md5="78431b5e5e0d4363f47799a819516fa8")

	depends_on("r-cli", type=("build", "run"))
	depends_on("r-coro@1.0.1:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-generics", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-hardhat", type=("build", "run"))
	depends_on("r-rlang@1.1.1:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-torch@0.11:", type=("build", "run"))
