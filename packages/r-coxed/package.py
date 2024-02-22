# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCoxed(RPackage):
	"""Duration-Based Quantities of Interest for the Cox Proportional
Hazards Model

	Functions for generating, simulating, and visualizing expected durations and marginal changes in duration from the Cox proportional hazards model as described in Kropko and Harden (2017) <doi:10.1017/S000712341700045X> and Harden and Kropko (2018) <doi:10.1017/psrm.2018.19>.
	"""
	
	homepage = "https://github.com/jkropko/coxed"
	cran = "coxed" 

	version("0.3.3", md5="8152e081ed9542525ee94323a8e3545d")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rms", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-permalgo", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-mediation", type=("build", "run"))
