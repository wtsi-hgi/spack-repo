# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCalibratessb(RPackage):
	"""Weighting and Estimation for Panel Data with Non-Response

	Functions to calculate weights, estimates of changes and corresponding variance estimates for panel data with non-response. Partially overlapping samples are handled. Initially, weights are calculated by linear calibration. By default, the survey package is used for this purpose. It is also possible to use ReGenesees, which can be installed from <https://github.com/DiegoZardetto/ReGenesees>. Variances of linear combinations (changes and averages) and ratios are calculated from a covariance matrix based on residuals according to the calibration model. The methodology was presented at the conference, The Use of R in Official Statistics, and is described in Langsrud (2016) <http://www.revistadestatistica.ro/wp-content/uploads/2016/06/RRS2_2016_A021.pdf>.  
	"""
	
	homepage = "https://github.com/statisticsnorway/CalibrateSSB"
	cran = "CalibrateSSB" 

	version("1.3.0", md5="a0895048d0f2b7bdace297c0ecc7206b")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-survey", type=("build", "run"))
