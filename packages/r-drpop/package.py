# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDrpop(RPackage):
	"""Efficient and Doubly Robust Population Size Estimation

	Estimation of the total population size from capture-recapture data efficiently and with low bias implementing the methods from Das M, Kennedy EH, and Jewell NP (2021) <arXiv:2104.14091>. The estimator is doubly robust against errors in the estimation of the intermediate nuisance parameters. Users can choose from the flexible estimation models provided in the package, or use any other preferred model.
	"""
	
	cran = "drpop" 

	version("0.0.3", md5="77317f3a799ff0116ccde64c5e782326")

	depends_on("r-gam", type=("build", "run"))
	depends_on("r-janitor", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-superlearner", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-nnet", type=("build", "run"))
	depends_on("r-nnls", type=("build", "run"))
	depends_on("r-ranger", type=("build", "run"))
