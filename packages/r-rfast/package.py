# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRfast(RPackage):
	"""A Collection of Efficient and Extremely Fast R Functions.

	A collection of fast (utility) functions for data analysis. Column- and
	row- wise means, medians, variances, minimums, maximums, many t, F and
	G-square tests, many regressions (normal, logistic, Poisson), are some of
	the many fast functions. References: a) Tsagris M., Papadakis M. (2018).
	Taking R to its limits: 70+ tips. PeerJ Preprints 6:e26605v1
	<doi:10.7287/peerj.preprints.26605v1>. b) Tsagris M. and Papadakis M.
	(2018). Forward regression in R: from the extreme slow to the extreme fast.
	Journal of Data Science, 16(4): 771-780.
	<doi:10.6339/JDS.201810_16(4).00006>."""

	cran = "Rfast"

	version("2.1.0", md5="ba455888bd71d3cbce27d29be5f1948c")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp@0.12.3:", type=("build", "run"))
	depends_on("r-rcppziggurat", type=("build", "run"))
	depends_on("r-rcppparallel", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
