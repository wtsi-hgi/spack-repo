# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMarketmatching(RPackage):
	"""Market Matching and Causal Impact Inference

	For a given test market find the best control markets using time series matching and analyze the impact of an intervention. The intervention could be a marketing event or some other local business tactic that is being tested. The workflow implemented in the Market Matching package utilizes dynamic time warping (the 'dtw' package) to do the matching and the 'CausalImpact' package to analyze the causal impact. In fact, this package can be considered a "workflow wrapper" for those two packages. In addition, if you don't have a chosen set of test markets to match, the Market Matching package can provide suggested test/control market pairs and pseudo prospective power analysis (measuring causal impact at fake interventions). 
	"""
	
	cran = "MarketMatching" 

	version("1.2.1", md5="e5a2b59d8ad1f40d9b3080c3857be4c9")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-iterators", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-causalimpact", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-bsts", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-boom", type=("build", "run"))
	depends_on("r-utf8", type=("build", "run"))
	depends_on("r-dtw", type=("build", "run"))
