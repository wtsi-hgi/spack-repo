# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNmaoutlier(RPackage):
	"""Detecting Outliers in Network Meta-Analysis

	A set of functions providing several outlier (i.e., studies with extreme findings) and influential detection measures and methodologies in network meta-analysis :
               - simple outlier and influential detection measures
               - outlier and influential detection measures by considering study deletion (shift the mean)
               - plots for outlier and influential detection measures
	       - Q-Q plot for network meta-analysis
               - Forward Search algorithm in network meta-analysis. 
               - forward plots to monitor statistics in each step of the forward search algorithm
               - forward plots for summary estimates and their confidence intervals in each step of forward search algorithm.   
	"""
	
	homepage = "https://github.com/petropouloumaria/NMAoutlier"
	cran = "NMAoutlier" 

	version("0.1.18", md5="2c14870ca376f00463223a25225485b6")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-netmeta@0.9.7:", type=("build", "run"))
	depends_on("r-meta@4.19.1:", type=("build", "run"))
	depends_on("r-mass@7.3.47:", type=("build", "run"))
	depends_on("r-reshape2@1.4.3:", type=("build", "run"))
	depends_on("r-ggplot2@3:", type=("build", "run"))
	depends_on("r-gridextra@2.3:", type=("build", "run"))
