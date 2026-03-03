# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWbsts(RPackage):
	"""Multiple Change-Point Detection for Nonstationary Time Series

	Implements detection for the number and locations of
    the change-points in a time series using the Wild Binary Segmentation and
    the Locally Stationary Wavelet model of Korkas and Fryzlewicz (2017) <doi:10.5705/ss.202015.0262>.
	"""
	
	cran = "wbsts" 

	version("2.1", md5="f0e8a66c966469b234de3977530ee603")

	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-wavelets", type=("build", "run"))
	depends_on("r@3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
