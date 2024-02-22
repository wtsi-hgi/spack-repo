# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStlplus(RPackage):
	"""Enhanced Seasonal Decomposition of Time Series by Loess

	Decompose a time series into seasonal, trend, and remainder
    components using an implementation of Seasonal Decomposition of Time
    Series by Loess (STL) that provides several enhancements over the STL
    method in the stats package.  These enhancements include handling missing
    values, providing higher order (quadratic) loess smoothing with automated
    parameter choices, frequency component smoothing beyond the seasonal and
    trend components, and some basic plot methods for diagnostics.
	"""
	
	homepage = "https://github.com/hafen/stlplus"
	cran = "stlplus" 

	version("0.5.1", md5="4e16199c9c4e56f4fb93f5470af44c40")

	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-yaimpute", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
