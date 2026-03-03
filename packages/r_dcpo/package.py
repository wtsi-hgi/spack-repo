# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDcpo(RPackage):
	"""Dynamic Comparative Public Opinion

	Estimates latent variables of public opinion cross-nationally and over time from sparse and incomparable survey data.  'DCPO' uses a population-level graded response model with country-specific item bias terms. Sampling is conducted with 'Stan'.  References: Solt (2020) <doi:10.31235/osf.io/d5n9p>.
	"""
	
	cran = "DCPO" 

	version("0.5.3", md5="0ed668794031dec8a82ebf9963ac0f37")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-rcpp@0.12:", type=("build", "run"))
	depends_on("r-rstan@2.18.1:", type=("build", "run"))
	depends_on("r-rstantools@2:", type=("build", "run"))
	depends_on("r-beepr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
	depends_on("r-janitor", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-stanheaders@2.18:", type=("build", "run"))
	depends_on("r-bh@1.66.0.1:", type=("build", "run"))
	depends_on("r-rcppeigen@0.3.3.4:", type=("build", "run"))
