# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPda(RPackage):
	"""Privacy-Preserving Distributed Algorithms

	A collection of privacy-preserving distributed algorithms for conducting multi-site data analyses. The regression analyses can be linear regression for continuous outcome, logistic regression for binary outcome, Cox proportional hazard regression for time-to event outcome, Poisson regression for count outcome, or multi-categorical regression for nominal or ordinal outcome. The PDA algorithm runs on a lead site and only requires summary statistics from collaborating sites, with one or few iterations. The package can be used together with the online system (<https://pda-ota.pdamethods.org/>) for safe and convenient collaboration. For more information, please visit our software websites: <https://github.com/Penncil/pda>, and <https://pdamethods.org/>.
	"""
	
	cran = "pda" 

	version("1.2.6", md5="0567a09b10317679f8edd1544a461eab")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-rvest", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-minqa", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-metafor", type=("build", "run"))
	depends_on("r-ordinal", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
