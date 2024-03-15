# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWrs2(RPackage):
	"""A Collection of Robust Statistical Methods

	A collection of robust statistical methods based on Wilcox' WRS functions. It implements robust t-tests (independent and dependent samples), robust ANOVA (including between-within subject designs), quantile ANOVA, robust correlation, robust mediation, and nonparametric ANCOVA models based on robust location measures.
	"""
	
	homepage = "https://r-forge.r-project.org/projects/psychor/"
	cran = "WRS2" 

	version("1.1-6", md5="1d680b11b9cdc32bfd9ea886b0754904", url="https://cran.r-project.org/src/contrib/WRS2_1.1-6.tar.gz")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-reshape", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
