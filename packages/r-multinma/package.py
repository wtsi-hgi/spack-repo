# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMultinma(RPackage):
	"""Bayesian Network Meta-Analysis of Individual and Aggregate Data

	Network meta-analysis and network meta-regression models for 
    aggregate data, individual patient data, and mixtures of both individual 
    and aggregate data using multilevel network meta-regression as described by
    Phillippo et al. (2020) <doi:10.1111/rssa.12579>. Models are estimated in a
    Bayesian framework using 'Stan'.
	"""
	
	homepage = "https://dmphillippo.github.io/multinma/"
	cran = "multinma" 

	version("0.6.1", md5="647205b82650ae586354d747c199fa3e")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-rcpp@0.12:", type=("build", "run"))
	depends_on("r-rcppparallel@5.0.1:", type=("build", "run"))
	depends_on("r-rstan@2.26:", type=("build", "run"))
	depends_on("r-rstantools@2:", type=("build", "run"))
	depends_on("r-rdpack@0.7:", type=("build", "run"))
	depends_on("r-tibble@2.1.3:", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-randtoolbox", type=("build", "run"))
	depends_on("r-copula", type=("build", "run"))
	depends_on("r-tidyr@1:", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-ggraph", type=("build", "run"))
	depends_on("r-ggplot2@3.3:", type=("build", "run"))
	depends_on("r-ggdist@2.1.1:", type=("build", "run"))
	depends_on("r-truncdist", type=("build", "run"))
	depends_on("r-bayesplot", type=("build", "run"))
	depends_on("r-bh@1.66:", type=("build", "run"))
	depends_on("r-rcppeigen@0.3.3.3:", type=("build", "run"))
	depends_on("r-stanheaders@2.26:", type=("build", "run"))
