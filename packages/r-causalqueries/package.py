# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCausalqueries(RPackage):
	"""Make, Update, and Query Binary Causal Models

	Users can declare binary causal models, update beliefs about causal types given data and calculate arbitrary estimands.  Model definition makes use of 'dagitty' functionality. Updating is implemented in 'stan'. The approach used in 'CausalQueries' is a generalization of the 'biqq' models described in "Mixing Methods: A Bayesian Approach" (Humphreys and Jacobs, 2015, <DOI:10.1017/S0003055415000453>). The conceptual extension makes use of work on probabilistic causal models described in Pearl's Causality (Pearl, 2009, <DOI:10.1017/CBO9780511803161>).
	"""
	
	cran = "CausalQueries" 

	version("1.0.2", md5="0dc613138887d03cfbb64118ee01b35a")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-rcpp@0.12:", type=("build", "run"))
	depends_on("r-dagitty@0.3.1:", type=("build", "run"))
	depends_on("r-dirmult@0.1.3.4:", type=("build", "run"))
	depends_on("r-rlang@0.2:", type=("build", "run"))
	depends_on("r-rstan@2.26:", type=("build", "run"))
	depends_on("r-rstantools@2:", type=("build", "run"))
	depends_on("r-stringr@1.4:", type=("build", "run"))
	depends_on("r-ggdag@0.2.4:", type=("build", "run"))
	depends_on("r-latex2exp@0.9.4:", type=("build", "run"))
	depends_on("r-ggplot2@3.3.5:", type=("build", "run"))
	depends_on("r-lifecycle@1.0.1:", type=("build", "run"))
	depends_on("r-bh@1.66:", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-rcppeigen@0.3.3.3:", type=("build", "run"))
	depends_on("r-stanheaders@2.26:", type=("build", "run"))
