# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGeomcomb(RPackage):
	"""(Geometric) Forecast Combination Methods

	Provides eigenvector-based (geometric) forecast
    combination methods; also includes simple approaches (simple average,
    median, trimmed and winsorized mean, inverse rank method) and regression-based
    combination. Tools for data pre-processing are available in order to deal with 
    common problems in forecast combination (missingness, collinearity).
	"""
	
	homepage = "https://github.com/ceweiss/GeomComb"
	cran = "GeomComb" 

	version("1.0", md5="e12944029bcf11d0a44690b61d2e646d")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-forecast@7.3:", type=("build", "run"))
	depends_on("r-forecastcombinations@1.1:", type=("build", "run"))
	depends_on("r-ggplot2@2.1:", type=("build", "run"))
	depends_on("r-matrix@1.2.6:", type=("build", "run"))
	depends_on("r-mtsdi@0.3.3:", type=("build", "run"))
	depends_on("r-psych@1.6.9:", type=("build", "run"))
