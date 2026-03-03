# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTcftt(RPackage):
	"""Two-Sample Tests for Skewed Data

	The classical two-sample t-test works well for the normally distributed data or 
    data with large sample size. The tcfu() and tt() tests implemented in this package provide 
    better type-I-error control with more accurate power when testing the equality of two-sample 
    means for skewed populations having unequal variances. These tests are especially useful 
    when the sample sizes are moderate. The tcfu() uses the Cornish-Fisher expansion to achieve 
    a better approximation to the true percentiles. The tt() provides transformations of the Welch's 
    t-statistic so that the sampling distribution become more symmetric. For more technical details, 
    please refer to Zhang (2019) <http://hdl.handle.net/2097/40235>.
	"""
	
	cran = "tcftt" 

	version("0.1.0", md5="90e7fb0c5eed6ca92d018a03e8ee6533")

	depends_on("r@3.1:", type=("build", "run"))
