# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBinsmooth(RPackage):
	"""Generate PDFs and CDFs from Binned Data

	Provides several methods for generating density functions
    based on binned data. Methods include step function, recursive
    subdivision, and optimized spline. Data are assumed to be nonnegative, 
    the top bin is assumed to have no upper bound, but the bin widths need
    be equal. All PDF smoothing methods maintain the areas specified by 
    the binned data. (Equivalently, all CDF smoothing methods interpolate 
    the points specified by the binned data.) In practice, an estimate for 
    the mean of the distribution should be supplied as an optional argument.
    Doing so greatly improves the reliability of statistics computed from 
    the smoothed density functions. Includes methods for estimating the Gini 
    coefficient, the Theil index, percentiles, and random deviates from a 
    smoothed distribution. Among the three methods, the optimized spline 
    (splinebins) is recommended for most purposes. The percentile and 
    random-draw methods should be regarded as experimental, and these methods 
    only support splinebins. 
	"""
	
	cran = "binsmooth" 

	version("0.2.2", md5="7e1f4d3d9212332926f52033191254b2")

	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-ineq", type=("build", "run"))
	depends_on("r-triangle", type=("build", "run"))
