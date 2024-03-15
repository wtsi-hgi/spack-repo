# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMcmsupply(RPackage):
	"""Estimating Public and Private Sector Contraceptive Market Supply
Shares

	Family Planning programs and initiatives typically use nationally representative surveys to estimate key indicators of a country’s family planning progress. However, in recent years, routinely collected family planning services data (Service Statistics) have been used as a supplementary data source to bridge gaps in the surveys. The use of service statistics comes with the caveat that adjustments need to be made for missing private sector contributions to the contraceptive method supply chain. Evaluating the supply source of modern contraceptives often relies on Demographic Health Surveys (DHS), where many countries do not have recent data beyond 2015/16. Fortunately, in the absence of recent surveys we can rely on statistical model-based estimates and projections to fill the knowledge gap. We present a Bayesian, hierarchical, penalized-spline model with multivariate-normal spline coefficients, to account for across method correlations, to produce country-specific,annual estimates for the proportion of modern contraceptive methods coming from the public and private sectors. This package provides a quick and convenient way for users to access the DHS modern contraceptive supply share data at national and subnational administration levels, estimate, evaluate and plot annual estimates with uncertainty for a sample of low- and middle-income countries. Methods for the estimation of method supply shares at the national level are described in Comiskey, Alkema, Cahill (2022) <arXiv:2212.03844>.
	"""
	
	homepage = "https://hannahcomiskey.github.io/mcmsupply/"
	cran = "mcmsupply" 

	version("1.0.1", md5="646453703b3d6dab98e72a40a0c30b28")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-r2jags", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-tidyverse", type=("build", "run"))
	depends_on("r-tidybayes", type=("build", "run"))
	depends_on("r-runjags", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
