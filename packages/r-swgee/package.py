# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSwgee(RPackage):
	"""Simulation Extrapolation Inverse Probability Weighted
Generalized Estimating Equations

	Simulation extrapolation and inverse probability weighted generalized estimating equations method for longitudinal data with missing observations and measurement error in covariates. References: Yi, G. Y. (2008) <doi:10.1093/biostatistics/kxm054>; Cook, J. R. and Stefanski, L. A. (1994) <doi:10.1080/01621459.1994.10476871>; Little, R. J. A. and Rubin, D. B. (2002, ISBN:978-0-471-18386-0).
	"""
	
	cran = "swgee" 

	version("1.4", md5="d6aa699fd64e8f8ac54ed7b4f9643eaf")

	depends_on("r-gee", type=("build", "run"))
	depends_on("r-geepack", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
