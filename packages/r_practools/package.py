# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPractools(RPackage):
	"""Designing and Weighting Survey Samples

	Functions and datasets to support Valliant, Dever, and Kreuter (2018), <doi:10.1007/978-3-319-93632-1>, "Practical Tools for Designing and Weighting Survey Samples". Contains functions for sample size calculation for survey samples using stratified or clustered one-, two-, and three-stage sample designs, and single-stage audit sample designs. Functions are included that will group geographic units accounting for distances apart and measures of size. Other functions compute variance components for multistage designs and sample sizes in two-phase designs. A number of example data sets are included.
	"""
	
	cran = "PracTools" 

	version("1.4.3", md5="b061a884b46aaaa9a92637c31a1018c3")
	version("1.4.2", md5="532a390359ba9519fec5220aeb13caa9")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-geosphere", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-usmap", type=("build", "run"))
