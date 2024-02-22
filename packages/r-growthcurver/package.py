# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGrowthcurver(RPackage):
	"""Simple Metrics to Summarize Growth Curves

	Fits the logistic equation to
    microbial growth curve data (e.g., repeated absorbance measurements
    taken from a plate reader over time). From this fit, a variety of
    metrics are provided, including the maximum growth rate,
    the doubling time, the carrying capacity, the area under the logistic
    curve, and the time to the inflection point. Method described in 
    Sprouffske and Wagner (2016) <doi:10.1186/s12859-016-1016-7>.
	"""
	
	homepage = "https://github.com/sprouffske/growthcurver"
	cran = "growthcurver" 

	version("0.3.1", md5="d4e0ae0bdfddf6caf1ba0eb38d19167a")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-minpack-lm@1.2:", type=("build", "run"))
