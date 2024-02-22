# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTipmap(RPackage):
	"""Tipping Point Analysis for Bayesian Dynamic Borrowing

	Tipping point analysis for clinical trials that employ Bayesian dynamic borrowing via robust meta-analytic predictive (MAP) priors. Further functions facilitate expert elicitation of a primary weight of the informative component of the robust MAP prior and computation of operating characteristics. Intended use is the planning, analysis and interpretation of extrapolation studies in pediatric drug development, but applicability is generally wider.
	"""
	
	homepage = "https://github.com/Boehringer-Ingelheim/tipmap"
	cran = "tipmap" 

	version("0.5.2", md5="0ce8904ae77045981200b2921b62484b")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rbest", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-furrr", type=("build", "run"))
	depends_on("r-future", type=("build", "run"))
