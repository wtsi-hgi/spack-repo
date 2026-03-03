# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMlmusingr(RPackage):
	"""Practical Multilevel Modeling

	Convenience functions and datasets to be used with Practical Multilevel Modeling using R. The package includes functions for calculating group means, group mean centered variables, and displaying some basic missing data information. A function for computing robust standard errors for linear mixed models based on Liang and Zeger (1986) <doi:10.1093/biomet/73.1.13> and Bell and 'McCaffrey' (2002) <https://www150.statcan.gc.ca/n1/en/pub/12-001-x/2002002/article/9058-eng.pdf?st=NxMjN1YZ> is included as well as a function for checking for level-one homoskedasticity (Raudenbush & Bryk, 2002, ISBN:076191904X).  
	"""
	
	homepage = "https://github.com/flh3/MLMusingR"
	cran = "MLMusingR" 

	version("0.3.2", md5="709cde55f9acf9e727bd09c056949f43")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-broom", type=("build", "run"))
	depends_on("r-generics", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-performance", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
