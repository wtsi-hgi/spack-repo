# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMerror(RPackage):
	"""Accuracy and Precision of Measurements

	N>=3 methods are used to measure each of n items. 
 The data are used to estimate simultaneously systematic error (bias)
 and random error (imprecision). Observed measurements for each method
 or device are assumed to be linear functions of the unknown true values
 and the errors are assumed normally distributed. Pairwise calibration
 curves and plots can be easily generated. Unlike the 'ncb.od' function,
 the 'omx' function builds a one-factor measurement error model using 'OpenMx'
 and allows missing values, uses full information maximum likelihood to 
 estimate parameters, and provides both likelihood-based and bootstrapped 
 confidence intervals for all parameters, in addition to Wald-type intervals.
	"""
	
	cran = "merror" 

	version("3.0", md5="a217a031af31c420401da6754baf7afa")

	depends_on("r-openmx", type=("build", "run"))
