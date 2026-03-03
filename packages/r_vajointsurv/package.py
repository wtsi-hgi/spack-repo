# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVajointsurv(RPackage):
	"""Variational Approximation for Joint Survival and Marker Models

	Estimates joint marker (longitudinal) and
    and survival (time-to-event) outcomes using variational approximations.
    The package supports multivariate markers allowing for
    correlated error terms and multiple types of survival outcomes which may be
    left-truncated, right-censored, and recurrent. Time-varying fixed and
    random covariate effects are supported along with non-proportional hazards.
	"""
	
	homepage = "https://github.com/boennecd/VAJointSurv"
	cran = "VAJointSurv" 

	version("0.1.0", md5="d3f9ebec3e5be56ebcefde43bd8d0acf")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-simsurvnmarker", type=("build", "run"))
	depends_on("r-psqn@0.3:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
	depends_on("r-testthat", type=("build", "run"))
