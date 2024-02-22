# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTeam(RPackage):
	"""Multiple Hypothesis Testing on an Aggregation Tree Method

	An implementation of the TEAM algorithm to identify local differences 
    between two (e.g. case and control) independent, univariate distributions, as 
    described in J Pura, C Chan, and J Xie (2019) <arXiv:1906.07757>. The algorithm 
    is based on embedding a multiple-testing procedure on a hierarchical structure 
    to identify high-resolution differences between two distributions. The 
    hierarchical structure is designed to identify strong, short-range differences 
    at lower layers and weaker, but long-range differences at increasing layers. 
    TEAM yields consistent layer-specific and overall false discovery rate control.
	"""
	
	cran = "TEAM" 

	version("0.1.0", md5="d0ee56318cf49f72560cdf7e96322af3")

	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ks", type=("build", "run"))
