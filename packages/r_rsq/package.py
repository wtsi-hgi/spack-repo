# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRsq(RPackage):
	"""R-Squared and Related Measures

	Calculate generalized R-squared, partial R-squared, and partial correlation coefficients for generalized linear (mixed) models (including quasi models with well defined variance functions).
	"""
	
	cran = "rsq" 

	version("2.6", md5="f03014bff15521bcb09ba73f207a8fc5")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-deriv", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-deming", type=("build", "run"))
