# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFsmumi(RPackage):
	"""Imputation of Time Series Based on Fuzzy Logic

	Filling large gaps in low or uncorrelated multivariate time series uses a new fuzzy weighted similarity measure. It contains all required functions to create large missing consecutive values within time series and then fill these gaps, according to the paper Phan et al. (2018), <DOI:10.1155/2018/9095683>. Performance indicators are also provided to compare similarity between two univariate signals (incomplete signal and imputed signal).
	"""
	
	homepage = "http://mawenzi.univ-littoral.fr/FSMUMI/"
	cran = "FSMUMI" 

	version("1.0", md5="850bac1156af22e1eda59b465df26fbd")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-fuzzyr", type=("build", "run"))
	depends_on("r-lsa", type=("build", "run"))
