# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIcebox(RPackage):
	"""Individual Conditional Expectation Plot Toolbox

	Implements Individual Conditional Expectation (ICE) plots, a tool for visualizing the model estimated by any supervised learning algorithm. ICE plots refine Friedman's partial dependence plot by graphing the functional relationship between the predicted response and a covariate of interest for individual observations. Specifically, ICE plots highlight the variation in the fitted values across the range of a covariate of interest, suggesting where and to what extent they may exist.
	"""
	
	cran = "ICEbox" 

	version("1.1.5", md5="d7bab1ae882414248c0a1f7daf67d3c5")

	depends_on("r-sfsmisc", type=("build", "run"))
