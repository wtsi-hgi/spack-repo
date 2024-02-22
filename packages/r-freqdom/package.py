# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFreqdom(RPackage):
	"""Frequency Domain Based Analysis: Dynamic PCA

	Implementation of dynamic principal component
    analysis (DPCA), simulation of VAR and VMA processes and frequency domain tools. 
    These frequency domain methods for dimensionality reduction of multivariate time series
    were introduced by David Brillinger in his book Time Series (1974). We follow implementation
    guidelines as described in Hormann, Kidzinski and Hallin (2016),
    Dynamic Functional Principal Component <doi:10.1111/rssb.12076>.
	"""
	
	cran = "freqdom" 

	version("2.0.3", md5="4a23a20f4a654a5596f77e5c29470a95")

	depends_on("r@2.15:", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-matrixcalc", type=("build", "run"))
