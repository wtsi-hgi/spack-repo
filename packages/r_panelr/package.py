# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPanelr(RPackage):
	"""Regression Models and Utilities for Repeated Measures and Panel
Data

	Provides an object type and associated tools for storing and 
  wrangling panel data. Implements several methods for creating regression
  models that take advantage of the unique aspects of 
  panel data. Among other capabilities, automates the "within-between" 
  (also known as "between-within" and "hybrid") panel regression specification
  that combines the desirable aspects of both fixed effects and random effects 
  econometric models and fits them as multilevel models 
  (Allison, 2009 <doi:10.4135/9781412993869.d33>; 
  Bell & Jones, 2015 <doi:10.1017/psrm.2014.7>). These models can also be 
  estimated via generalized estimating equations 
  (GEE; McNeish, 2019 <doi:10.1080/00273171.2019.1602504>) and Bayesian 
  estimation is (optionally) supported via 'Stan'. 
  Supports estimation of asymmetric effects models via first differences
  (Allison, 2019 <doi:10.1177/2378023119826441>) as well as a generalized
  linear model extension thereof using GEE. 
	"""
	
	homepage = "https://panelr.jacob-long.com"
	cran = "panelr" 

	version("0.7.8", md5="7f6a1ee6789f248de7503c1fa95f58f5")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-formula", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-jtools@2.0.1:", type=("build", "run"))
	depends_on("r-lmertest", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang@0.3:", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble@2:", type=("build", "run"))
	depends_on("r-tidyr@0.8.3:", type=("build", "run"))
