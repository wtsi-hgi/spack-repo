# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTwopartm(RPackage):
	"""Two-Part Model with Marginal Effects

	Fit two-part regression models for zero-inflated data. The models and their components are represented using S4 classes and methods. Average Marginal effects and predictive margins with standard errors and
  confidence intervals can be calculated from two-part model objects. Belotti, F., Deb, P., Manning, W. G., & Norton, E. C. (2015) <doi:10.1177/1536867X1501500102>.
	"""
	
	cran = "twopartm" 

	version("0.1.0", md5="129172e93b9bc355292cfeb83f429abe")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
