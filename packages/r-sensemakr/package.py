# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSensemakr(RPackage):
	"""Sensitivity Analysis Tools for Regression Models

	Implements a suite of sensitivity analysis tools 
  that extends the traditional omitted variable bias framework and makes it easier 
  to understand the impact of omitted variables in regression models, as discussed in Cinelli, C. and Hazlett, C. (2020), "Making Sense of Sensitivity: Extending Omitted Variable Bias." Journal of the Royal Statistical Society, Series B (Statistical Methodology) <doi:10.1111/rssb.12348>.
	"""
	
	homepage = "https://github.com/carloscinelli/sensemakr"
	cran = "sensemakr" 

	version("0.1.4", md5="fd15b1d40717f4b4780822e046e33984")

	depends_on("r@3.1:", type=("build", "run"))
