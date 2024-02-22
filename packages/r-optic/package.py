# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROptic(RPackage):
	"""Simulation Tool for Causal Inference Using Longitudinal Data

	Implements a simulation study to assess the strengths and
    weaknesses of causal inference methods for estimating policy effects
    using panel data. See Griffin et al. (2021)
    <doi:10.1007/s10742-022-00284-w> and Griffin et al. (2022)
    <doi:10.1186/s12874-021-01471-y> for a description of our methods.
	"""
	
	homepage = "https://randcorporation.github.io/optic/"
	cran = "optic" 

	version("1.0.1", md5="fc107f0e27435dd5ec8bdd462070e354")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-did", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-future-apply", type=("build", "run"))
	depends_on("r-lmtest", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-sandwich", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
