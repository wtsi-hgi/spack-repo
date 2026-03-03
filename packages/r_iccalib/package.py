# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIccalib(RPackage):
	"""Cox Model with Interval-Censored Starting Time of a Covariate

	Calibration and risk-set calibration methods for fitting Cox proportional hazard model when a binary covariate is measured intermittently. Methods include functions to fit calibration models from interval-censored data and modified partial likelihood for the proportional hazard model, Nevo et al. (2018+) <arXiv:1801.01529>.
	"""
	
	cran = "ICcalib" 

	version("1.0.8", md5="a8ff3ce6e305156990e99cf26677a717")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-fitdistrplus", type=("build", "run"))
	depends_on("r-icenreg", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-icsurv", type=("build", "run"))
	depends_on("r-msm", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
