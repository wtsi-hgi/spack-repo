# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRobustbetareg(RPackage):
	"""Robust Beta Regression

	Robust estimators for the beta regression, useful for modeling 
  bounded continuous data. Currently, four types of robust estimators are supported. 
  They depend on a tuning constant which may be fixed or selected by a 
  data-driven algorithm also implemented in the package. Diagnostic tools 
  associated with the fitted model, such as the residuals and goodness-of-fit 
  statistics, are implemented. Robust Wald-type tests are available. More details
  about robust beta regression are described in Maluf et al. (2022) <arXiv:2209.11315>.
	"""
	
	cran = "robustbetareg" 

	version("0.3.0", md5="17d45c11d209f87996859b444b94af02")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-betareg", type=("build", "run"))
	depends_on("r-rmpfr", type=("build", "run"))
	depends_on("r-rstudioapi", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-formula", type=("build", "run"))
	depends_on("r-robustbase", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-bbmisc", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-misctools", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
