# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBnpdensity(RPackage):
	"""Ferguson-Klass Type Algorithm for Posterior Normalized Random
Measures

	Bayesian nonparametric density estimation modeling mixtures by a Ferguson-Klass type algorithm for posterior normalized random measures.
	"""
	
	cran = "BNPdensity" 

	version("2023.3.8", md5="43075af2ba1c0b43cd451097162ce52f")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-viridis", type=("build", "run"))
