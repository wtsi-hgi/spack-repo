# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCtsfeatures(RPackage):
	"""Analyzing Categorical Time Series

	An implementation of several functions for feature extraction in 
    categorical time series datasets. Specifically, some features related to 
    marginal distributions and serial dependence patterns can be computed. These 
    features can be used to feed clustering and classification algorithms for
    categorical time series, among others. The package also includes some
    interesting datasets containing biological sequences. Practitioners from a 
    broad variety of fields could benefit from the general framework provided 
    by 'ctsfeatures'.
	"""
	
	cran = "ctsfeatures" 

	version("1.2.2", md5="25ffdd831d03127cb573661139ad239d")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-astsa", type=("build", "run"))
	depends_on("r-latex2exp", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-bolstad2", type=("build", "run"))
	depends_on("r-tsibble", type=("build", "run"))
