# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCopulacenr(RPackage):
	"""Copula-Based Regression Models for Multivariate Censored Data

	Copula-based regression models for multivariate censored data, including 
 bivariate right-censored data, bivariate interval-censored data, and right/interval-censored 
 semi-competing risks data. Currently supports Clayton, Gumbel, Frank, Joe, AMH and 
 Copula2 copula models. For marginal models, it supports parametric (Weibull, Loglogistic, 
 Gompertz) and semiparametric (Cox and transformation) models. Includes methods for 
 convenient prediction and plotting. Also provides a bivariate time-to-event simulation 
 function and an information ratio-based goodness-of-fit test for copula. Method details 
 can be found in Sun et.al (2019) Lifetime Data Analysis, Sun et.al (2021) Biostatistics, 
 Sun et.al (2022) Statistical Methods in Medical Research, Sun et.al (2022) Biometrics, and
 Sun et al. (2023+) JRSSC.
	"""
	
	cran = "CopulaCenR" 

	version("1.2.3", md5="09c837802cbb16c8b641e55c0e3cd2de")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
	depends_on("r-copbasic", type=("build", "run"))
	depends_on("r-copula", type=("build", "run"))
	depends_on("r-corpcor", type=("build", "run"))
	depends_on("r-flexsurv", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-icenreg", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-vinecopula", type=("build", "run"))
