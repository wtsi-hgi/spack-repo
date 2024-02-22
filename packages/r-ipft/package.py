# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIpft(RPackage):
	"""Indoor Positioning Fingerprinting Toolset

	Algorithms and utility functions for indoor positioning using fingerprinting techniques. 
    These functions are designed for manipulation of RSSI (Received Signal Strength Intensity) data 
    sets, estimation of positions,comparison of the performance of different models, and graphical 
    visualization of data. Machine learning algorithms and methods such as k-nearest neighbors or
    probabilistic fingerprinting are implemented in this package to perform analysis
    and estimations over RSSI data sets.
	"""
	
	cran = "ipft" 

	version("0.7.2", md5="7ccd8c18ac19f5bd1d277761cae77232")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-apcluster", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
