# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCdcatr(RPackage):
	"""Cognitive Diagnostic Computerized Adaptive Testing

	Provides a set of functions for conducting cognitive diagnostic computerized adaptive testing applications (Chen, 2009) <DOI:10.1007/s11336-009-9123-2>). It includes different item selection rules such us the global discrimination index (Kaplan, de la Torre, and Barrada (2015) <DOI:10.1177/0146621614554650>) and the nonparametric selection method (Chang, Chiu, and Tsai (2019) <DOI:10.1177/0146621618813113>), as well as several stopping rules. Functions for generating item banks and responses are also provided. To guide item bank calibration, model comparison at the item level can be conducted using the two-step likelihood ratio test statistic by Sorrel, de la Torre, Abad and Olea (2017) <DOI:10.1027/1614-2241/a000131>.
	"""
	
	homepage = "https://github.com/miguel-sorrel/cdcatR"
	cran = "cdcatR" 

	version("1.0.6", md5="9c6f2b9054583855f8377c993df7b630")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-cdmtools@1.0.1:", type=("build", "run"))
	depends_on("r-gdina@2.2:", type=("build", "run"))
	depends_on("r-ggplot2@3.3:", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-dosnow", type=("build", "run"))
	depends_on("r-npcd", type=("build", "run"))
