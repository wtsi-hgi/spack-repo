# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLdats(RPackage):
	"""Latent Dirichlet Allocation Coupled with Time Series Analyses

	Combines Latent Dirichlet Allocation (LDA) and Bayesian multinomial time series methods in a two-stage analysis to quantify dynamics in high-dimensional temporal data. LDA decomposes multivariate data into lower-dimension latent groupings, whose relative proportions are modeled using generalized Bayesian time series models that include abrupt changepoints and smooth dynamics. The methods are described in Blei et al. (2003) <doi:10.1162/jmlr.2003.3.4-5.993>, Western and Kleykamp (2004) <doi:10.1093/pan/mph023>, Venables and Ripley (2002, ISBN-13:978-0387954578), and Christensen et al. (2018) <doi:10.1002/ecy.2373>.
	"""
	
	homepage = "https://weecology.github.io/LDATS/"
	cran = "LDATS" 

	version("0.3.0", md5="1672c68e30d982269914693ac7309e62")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-extradistr", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-memoise", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-nnet", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
	depends_on("r-topicmodels", type=("build", "run"))
	depends_on("r-viridis", type=("build", "run"))
	depends_on("gsl", type=("build", "link", "run"))
