# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQtools(RPackage):
	"""Utilities for Quantiles

	Functions for unconditional and conditional quantiles. These
    include methods for transformation-based quantile regression,
    quantile-based measures of location, scale and shape, methods for quantiles
    of discrete variables, quantile-based multiple imputation, restricted
    quantile regression, directional quantile classification, and quantile
	ratio regression.
	A vignette is given in Geraci (2016, The R Journal) <doi:10.32614/RJ-2016-037> and included in the package.
	"""
	
	cran = "Qtools" 

	version("1.5.9", md5="7a57782aaab4299bde2b7fb59af90846")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-conquer", type=("build", "run"))
	depends_on("r-glmx", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-np", type=("build", "run"))
	depends_on("r-numderiv@2016.8.1:", type=("build", "run"))
	depends_on("r-quantdr", type=("build", "run"))
	depends_on("r-quantreg", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
