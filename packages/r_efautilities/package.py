# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REfautilities(RPackage):
	"""Utility Functions for Exploratory Factor Analysis

	A number of utility function for exploratory factor analysis are included in this package. In particular, it computes standard errors for parameter estimates and factor correlations under a variety of conditions.
	"""
	
	cran = "EFAutilities" 

	version("2.1.3", md5="7dfbf5305e8416f133c3e56134066ccc")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-gparotation", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
