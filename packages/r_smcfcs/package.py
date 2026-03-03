# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSmcfcs(RPackage):
	"""Multiple Imputation of Covariates by Substantive Model
Compatible Fully Conditional Specification

	Implements multiple imputation of missing covariates by
    Substantive Model Compatible Fully Conditional Specification.
    This is a modification of the popular FCS/chained equations
    multiple imputation approach, and allows imputation of missing
    covariate values from models which are compatible with the user
    specified substantive model.
	"""
	
	homepage = "https://github.com/jwb133/smcfcs"
	cran = "smcfcs" 

	version("1.7.1", md5="f818f3d57bb56f05587ea94acd11d8d6")

	depends_on("r@3.1.2:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-vgam", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-brglm2", type=("build", "run"))
