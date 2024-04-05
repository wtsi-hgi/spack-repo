# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGeorob(RPackage):
	"""Robust Geostatistical Analysis of Spatial Data

	Provides functions for efficiently fitting linear models with spatially correlated errors by robust (Kuensch et al. (2011) <doi:10.3929/ethz-a-009900710>) and Gaussian (Harville (1977) <doi:10.1080/01621459.1977.10480998>) (Restricted) Maximum Likelihood and for computing robust and customary point and block external-drift Kriging predictions (Cressie (1993) <doi:10.1002/9781119115151>), along with utility functions for variogram modelling in ad hoc geostatistical analyses, model building, model evaluation by cross-validation, (conditional) simulation of Gaussian processes (Davies and Bryant (2013) <doi:10.18637/jss.v055.i09>), unbiased back-transformation of Kriging predictions of log-transformed data (Cressie (2006) <doi:10.1007/s11004-005-9022-8>).
	"""
	
	cran = "georob" 

	version("0.3-19", md5="0c78c1aa4f91c23f74cefe76f5781b64")
	version("0.3-18", md5="03b96a543f96d422e3c5fee652bb2308")

	depends_on("r@2.14:", type=("build", "run"))
	depends_on("r-sp@0.9.60:", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-constrainedkriging@0.2.7:", type=("build", "run"))
	depends_on("r-fields", type=("build", "run"))
	depends_on("r-lmtest", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-nleqslv", type=("build", "run"))
	depends_on("r-quantreg", type=("build", "run"))
	depends_on("r-robustbase@0.90.2:", type=("build", "run"))
	depends_on("r-snowfall", type=("build", "run"))
