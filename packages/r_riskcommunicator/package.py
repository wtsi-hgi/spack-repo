# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRiskcommunicator(RPackage):
	"""G-Computation to Estimate Interpretable Epidemiological Effects

	Estimates flexible epidemiological effect measures including both differences and ratios using the parametric G-formula developed as an alternative to inverse probability weighting.  It is useful for estimating the impact of interventions in the presence of treatment-confounder-feedback. G-computation was originally described by Robbins (1986) <doi:10.1016/0270-0255(86)90088-6> and has been described in detail by Ahern, Hubbard, and Galea (2009) <doi:10.1093/aje/kwp015>; Snowden, Rose, and Mortimer (2011) <doi:10.1093/aje/kwq472>; and Westreich et al. (2012) <doi:10.1002/sim.5316>.
	"""
	
	cran = "riskCommunicator" 

	version("1.0.1", md5="bf53101e485732e25163faa0f2d4679e")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
