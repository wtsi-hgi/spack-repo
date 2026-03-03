# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RExtremogram(RPackage):
	"""Estimation of Extreme Value Dependence for Time Series Data

	Estimation of the sample univariate, cross and return time extremograms. The package can also adds empirical confidence bands to each of the extremogram plots via a permutation procedure under the assumption that the data are independent. Finally, the stationary bootstrap allows us to construct credible confidence bands for the extremograms.  
	"""
	
	cran = "extremogram" 

	version("1.0.2", md5="4f72951d97e3757be664a95e9e50de3f")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-boot@1.3.11:", type=("build", "run"))
	depends_on("r-mass@7.3.31:", type=("build", "run"))
