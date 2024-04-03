# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPencal(RPackage):
	"""Penalized Regression Calibration (PRC) for the Dynamic
Prediction of Survival

	Computes penalized regression calibration (PRC), a
    statistical method for the dynamic prediction of survival when many
    longitudinal predictors are available. PRC is described in Signorelli
    et al.  (2021) <doi:10.1002/sim.9178> and Signorelli (2023)
    <doi:10.48550/arXiv.2309.15600>.
	"""
	
	homepage = "https://mirkosignorelli.github.io/r"
	cran = "pencal" 

	version("2.2.1", md5="0c3a941629e71a6a4f00acc5fe67059d")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-lcmm", type=("build", "run"))
	depends_on("r-magic", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-riskregression", type=("build", "run"))
	depends_on("r-survcomp", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-survivalroc", type=("build", "run"))
