# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RObliquersf(RPackage):
	"""Oblique Random Forests for Right-Censored Time-to-Event Data

	Oblique random survival forests incorporate linear combinations of input variables into random survival forests (Ishwaran, 2008 <DOI:10.1214/08-AOAS169>). Regularized Cox proportional hazard models (Simon, 2016 <DOI:10.18637/jss.v039.i05>) are used to identify optimal linear combinations of input variables. 
	"""
	
	cran = "obliqueRSF" 

	version("0.1.2", md5="e98f715a34d9c24b74544be7237539f5")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-pec", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-missforest", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-prodlim", type=("build", "run"))
	depends_on("r-ggthemes", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
