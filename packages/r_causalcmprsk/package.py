# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCausalcmprsk(RPackage):
	"""Nonparametric and Cox-Based Estimation of Average Treatment
Effects in Competing Risks

	Estimation of average treatment effects (ATE) of point interventions on time-to-event outcomes with K competing risks (K can be 1). The method uses propensity scores and inverse probability weighting for emulation of baseline randomization, which is described in Charpignon et al. (2022) <doi:10.1038/s41467-022-35157-w>.
	"""
	
	homepage = "https://github.com/Bella2001/causalCmprsk"
	cran = "causalCmprsk" 

	version("2.0.0", md5="5307ef64496a06fb6524d89489fef6b4")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-inline", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
