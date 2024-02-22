# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMlergm(RPackage):
	"""Multilevel Exponential-Family Random Graph Models

	Estimates exponential-family random graph models for multilevel network data, assuming the multilevel structure is observed. The scope, at present, covers multilevel models where the set of nodes is nested within known blocks. The estimation method uses Monte-Carlo maximum likelihood estimation (MCMLE) methods to estimate a variety of canonical or curved exponential family models for binary random graphs. MCMLE methods for curved exponential-family random graph models can be found in Hunter and Handcock (2006) <DOI: 10.1198/106186006X133069>. The package supports parallel computing, and provides methods for assessing goodness-of-fit of models and visualization of networks. 
	"""
	
	cran = "mlergm" 

	version("0.8", md5="6a527b93e44e0a1b42c63138196e153d")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-ergm@3.10.1:", type=("build", "run"))
	depends_on("r-network@1.15:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-ggally", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-lpsolve", type=("build", "run"))
	depends_on("r-sna@2.4:", type=("build", "run"))
