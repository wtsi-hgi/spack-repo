# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCna(RPackage):
	"""Causal Modeling with Coincidence Analysis

	Provides comprehensive functionalities for causal modeling with Coincidence Analysis (CNA), which is a configurational comparative method of causal data analysis that was first introduced in Baumgartner (2009) <doi:10.1177/0049124109339369>, and generalized in Baumgartner & Ambuehl (2018) <doi:10.1017/psrm.2018.45>. CNA is designed to recover INUS-causation from data, which is particularly relevant for analyzing processes featuring conjunctural causation (component causation) and equifinality (alternative causation). CNA is currently the only method for INUS-discovery that allows for multiple effects (outcomes/endogenous factors), meaning it can analyze common-cause and causal chain structures.
	"""
	
	homepage = "https://CRAN.R-project.org/package=cna"
	cran = "cna" 

	version("3.5.6", md5="53698cee16fec671fca5d75d2efd9a50")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-car", type=("build", "run"))
