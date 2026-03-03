# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RThesface(RPackage):
	"""The Subtype Free Average Causal Effect

	Estimation of the SF-ACE, a Causal Inference estimand proposed in the paper "The Subtype-Free Average Causal Effect For Heterogeneous Disease Etiology" (soon on arXiv).
	"""
	
	cran = "TheSFACE" 

	version("0.1.0", md5="63a8523464308f7793d2603ad10ad7dc")

	depends_on("r-nnet", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
