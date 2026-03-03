# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REirm(RPackage):
	"""Explanatory Item Response Modeling for Dichotomous and
Polytomous Items

	Analysis of dichotomous and polytomous response data using the explanatory item response modeling framework, as described in Bulut, Gorgun, & Yildirim-Erbasli (2021) <doi:10.3390/psych3030023>, Stanke & Bulut (2019) <doi:10.21449/ijate.515085>, and De Boeck & Wilson (2004) <doi:10.1007/978-1-4757-3990-9>. Generalized linear mixed modeling is used for estimating the effects of item-related and person-related variables on dichotomous and polytomous item responses. 
	"""
	
	homepage = "https://github.com/okanbulut/eirm"
	cran = "eirm" 

	version("0.5", md5="cc6be263135d7b8fb167654db4215733")

	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-blme", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-optimx", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinydashboard", type=("build", "run"))
	depends_on("r-shinycssloaders", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-ggeffects", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
