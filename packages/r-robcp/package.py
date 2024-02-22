# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRobcp(RPackage):
	"""Robust Change-Point Tests

	Provides robust methods to detect change-points in uni- or multivariate time series. They can cope with corrupted data and heavy tails. Focus is on the detection of abrupt changes in location, but changes scale or dependence structure can be detected as well. This package provides tests for change detection in uni- and multivariate time series based on Huberized versions of CUSUM tests proposed in Duerre and Fried (2019) <arXiv:1905.06201>, and tests for change detection in univariate time series based on 2-sample U-statistics or 2-sample U-quantiles as proposed by Dehling et al. (2015) <DOI:10.1007/978-1-4939-3076-0_12> and Dehling, Fried and Wendler (2020) <DOI:10.1093/biomet/asaa004>. Furthermore, the packages provides tests on changes in the scale or the correlation as proposed in Gerstenberger, Vogel and Wendler (2020) <DOI:10.1080/01621459.2019.1629938>, Dehling et al. (2017) <DOI:10.1017/S026646661600044X>, and Wied et al. (2014) <DOI:10.1016/j.csda.2013.03.005>.
	"""
	
	cran = "robcp" 

	version("0.3.7", md5="5086c7b294604ec4d3a2c1149dcc1682")

	depends_on("r@3.3.1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
