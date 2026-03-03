# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSjstats(RPackage):
	"""Collection of Convenient Functions for Common Statistical
Computations

	Collection of convenient functions for common statistical computations,
             which are not directly provided by R's base or stats packages.
             This package aims at providing, first, shortcuts for statistical measures, 
             which otherwise could only be calculated with additional effort 
             (like Cramer's V, Phi, or effect size statistics like Eta or Omega squared), 
             or for which currently no functions available. Second, another focus 
             lies on weighted variants of common statistical measures and tests 
             like weighted standard error, mean, t-test, correlation, and more.
	"""
	
	homepage = "https://strengejacke.github.io/sjstats/"
	cran = "sjstats" 

	version("0.18.2", md5="1f47ada9e1aba0129c6bfd42a14911aa")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-bayestestr", type=("build", "run"))
	depends_on("r-broom", type=("build", "run"))
	depends_on("r-datawizard", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-effectsize", type=("build", "run"))
	depends_on("r-emmeans", type=("build", "run"))
	depends_on("r-insight", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-modelr", type=("build", "run"))
	depends_on("r-parameters", type=("build", "run"))
	depends_on("r-performance", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-sjlabelled", type=("build", "run"))
	depends_on("r-sjmisc", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
