# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPanelmatch(RPackage):
	"""Matching Methods for Causal Inference with Time-Series
Cross-Sectional Data

	Implements a set of methodological tools
	     that enable researchers to apply matching methods to
	     time-series cross-sectional data. Imai, Kim, and Wang
	     (2021) <http://web.mit.edu/insong/www/pdf/tscs.pdf> 
	     proposes a nonparametric generalization of the
	     difference-in-differences estimator, which does not rely
	     on the linearity assumption as often done in
	     practice. Researchers first select a method of matching
	     each treated observation for a given unit in a
	     particular time period with control observations from
	     other units in the same time period that have a similar
	     treatment and covariate history. These methods include
	     standard matching methods based on propensity score and
	     Mahalanobis distance, as well as weighting methods. Once 
	     matching is done, both short-term and long-term average 
	     treatment effects for the treated can be estimated with 
	     standard errors. The package also offers a visualization 
	     technique that allows researchers to assess the quality 
	     of matches by examining the resulting covariate balance.
	"""
	
	cran = "PanelMatch" 

	version("2.0.1", md5="78d00666d85f49f6eb4b5b786b216ac3")

	depends_on("r@2.14:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-cbps", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
