# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDirttee(RPackage):
	"""Distributional Regression for Time to Event Data

	Semiparametric distributional regression methods (expectile,
    quantile and mode regression) for time-to-event variables with
    right-censoring; uses inverse probability of censoring weights or
    accelerated failure time models with auxiliary likelihoods. Expectile
    regression using inverse probability of censoring weights has been
    introduced in Seipp et al. (2021) ``Weighted Expectile Regression for
    Right-Censored Data'' <doi:10.1002/sim.9137>, mode regression for
    time-to-event variables has been introduced in Seipp et al. (2022)
    ``Flexible Semiparametric Mode Regression for Time-to-Event Data''
    <doi:10.1177/09622802221122406>.
	"""
	
	cran = "dirttee" 

	version("1.0.2", md5="763a51d6a644ec6f5d8e9dc58fd26c9e")

	depends_on("r-expectreg@0.5:", type=("build", "run"))
	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-formula-tools", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-nloptr", type=("build", "run"))
	depends_on("r-provenance", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
