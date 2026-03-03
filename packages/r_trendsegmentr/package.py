# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTrendsegmentr(RPackage):
	"""Linear Trend Segmentation

	Performs the detection of linear trend changes for univariate time series 
    by implementing the bottom-up unbalanced wavelet transformation proposed by 
    H. Maeng and P. Fryzlewicz (2023). The estimated number and locations of the 
    change-points are returned with the piecewise-linear estimator for signal.
	"""
	
	cran = "trendsegmentR" 

	version("1.3.0", md5="5429458fbccb864273ce8f04cdea557a")

