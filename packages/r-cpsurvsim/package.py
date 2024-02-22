# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCpsurvsim(RPackage):
	"""Simulating Survival Data from Change-Point Hazard Distributions

	Simulates time-to-event data
    with type I right censoring using two methods: the inverse CDF
    method and our proposed memoryless method. The latter method
    takes advantage of the memoryless property of survival and
    simulates a separate distribution between change-points. We
    include two parametric distributions: exponential and Weibull.
    Inverse CDF method draws on the work of Rainer Walke (2010), 
    <https://www.demogr.mpg.de/papers/technicalreports/tr-2010-003.pdf>.
	"""
	
	homepage = "https://github.com/camillejo/cpsurvsim"
	cran = "cpsurvsim" 

	version("1.2.2", md5="49887e385d3247e97debd3767d9de90d")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-plyr@1.8.5:", type=("build", "run"))
	depends_on("r-hmisc@4.3:", type=("build", "run"))
	depends_on("r-knitr@1.27:", type=("build", "run"))
