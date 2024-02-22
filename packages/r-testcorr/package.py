# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTestcorr(RPackage):
	"""Testing Zero Correlation

	Computes the test statistics for examining the significance of autocorrelation in univariate time series, cross-correlation in bivariate time series, Pearson correlations in multivariate series and test statistics for i.i.d. property of univariate series given in Dalla, Giraitis and Phillips (2020), <https://cowles.yale.edu/sites/default/files/files/pub/d21/d2194-r.pdf>.
	"""
	
	cran = "testcorr" 

	version("0.2.0", md5="65f45a37b0f80c3fc345165c31a75020")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
