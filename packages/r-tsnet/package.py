# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTsnet(RPackage):
	"""Fitting, Comparing, and Visualizing Networks Based on Time
Series Data

	Fit, compare, and visualize Bayesian graphical vector autoregressive (GVAR) network models using 'Stan'. These models are commonly used in psychology to represent temporal and contemporaneous relationships between multiple variables in intensive longitudinal data. Fitted models can be compared with a test based on matrix norm differences of posterior point estimates to quantify the differences between two estimated networks. See also Siepe, Kloft & Heck (2024) <doi:10.31234/osf.io/uwfjc>.
	"""
	
	homepage = "https://github.com/bsiepe/tsnet"
	cran = "tsnet" 

	version("0.1.0", md5="8ccdc7510c9d34ad9011bc76d9726a0a")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggdist", type=("build", "run"))
	depends_on("r-ggokabeito", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-posterior", type=("build", "run"))
	depends_on("r-rcpp@0.12:", type=("build", "run"))
	depends_on("r-rcppparallel@5.0.1:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rstan@2.18.1:", type=("build", "run"))
	depends_on("r-rstantools@2.3.1.1:", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-bh@1.66:", type=("build", "run"))
	depends_on("r-rcppeigen@0.3.3.3:", type=("build", "run"))
	depends_on("r-stanheaders@2.18:", type=("build", "run"))
