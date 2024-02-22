# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RForecastcomb(RPackage):
	"""Forecast Combination Methods

	Provides geometric- and regression-based forecast
    combination methods under a unified user interface for the packages 'ForecastCombinations'
    and 'GeomComb'. Additionally, updated tools and convenience functions for data pre-processing are available in order to deal with 
    common problems in forecast combination (missingness, collinearity). For method details see Hsiao C, Wan SK (2014). <doi:10.1016/j.jeconom.2013.11.003>, Hansen BE (2007). <doi:10.1111/j.1468-0262.2007.00785.x>,
    Elliott G, Gargano A, Timmermann A (2013). <doi:10.1016/j.jeconom.2013.04.017>, 
    and Clemen RT (1989). <doi:10.1016/0169-2070(89)90012-5>.
	"""
	
	homepage = "https://github.com/ceweiss/ForecastComb"
	cran = "ForecastComb" 

	version("1.3.1", md5="c543e866562c188ff3ea2f2c4f3e03f0")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-forecast@7.3:", type=("build", "run"))
	depends_on("r-ggplot2@2.1:", type=("build", "run"))
	depends_on("r-matrix@1.2.6:", type=("build", "run"))
	depends_on("r-mtsdi@0.3.3:", type=("build", "run"))
	depends_on("r-psych@1.6.9:", type=("build", "run"))
	depends_on("r-quadprog@1.5.5:", type=("build", "run"))
	depends_on("r-quantreg@5.29:", type=("build", "run"))
