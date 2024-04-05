# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBayesnec(RPackage):
	"""A Bayesian No-Effect- Concentration (NEC) Algorithm

	Implementation of No-Effect-Concentration estimation that uses 'brms' (see Burkner (2017)<doi:10.18637/jss.v080.i01>; Burkner (2018)<doi:10.32614/RJ-2018-017>; Carpenter 'et al.' (2017)<doi:10.18637/jss.v076.i01> to fit concentration(dose)-response data using Bayesian methods for the purpose of estimating 'ECx' values, but more particularly 'NEC' (see Fox (2010)<doi:10.1016/j.ecoenv.2009.09.012>), 'NSEC' (see Fisher and Fox (2023)<doi:10.1002/etc.5610>), and 'N(S)EC (see Fisher et al. 2023<doi:10.1002/ieam.4809>). This package expands and supersedes an original version implemented in R2jags, see Fisher, Ricardo and Fox (2020)<doi:10.5281/ZENODO.3966864>.
	"""
	
	homepage = "https://open-aims.github.io/bayesnec/"
	cran = "bayesnec" 

	version("2.1.2.0", md5="e0a846de03e11387f510e5b933f03498")
	version("2.1.1.0", md5="e0763f7c5546e780aebfdfd3db2f87cc")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-brms", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-formula-tools", type=("build", "run"))
	depends_on("r-loo", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-evaluate", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-chk@0.7:", type=("build", "run"))
