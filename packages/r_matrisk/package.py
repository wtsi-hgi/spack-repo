# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMatrisk(RPackage):
	"""Macroeconomic-at-Risk

	The Macroeconomics-at-Risk (MaR) approach is based on a two-step semi-parametric estimation procedure that allows to forecast the full conditional distribution of an economic variable at a given horizon, as a function of a set of factors. These density forecasts are then be used to produce coherent forecasts for any downside risk measure, e.g., value-at-risk, expected shortfall, downside entropy. Initially introduced by Adrian et al. (2019) <doi:10.1257/aer.20161923> to reveal the vulnerability of economic growth to financial conditions, the MaR approach is currently extensively used by international financial institutions to provide Value-at-Risk (VaR) type forecasts for GDP growth (Growth-at-Risk) or inflation (Inflation-at-Risk). This package provides methods for estimating these models. Datasets for the US and the Eurozone are available to allow testing of the Adrian et al (2019) model. This package constitutes a useful toolbox (data and functions) for private practitioners, scholars as well as policymakers.
	"""
	
	cran = "matrisk" 

	version("0.1.0", md5="334f6b1fbcfa4d856c9aa31736a6a5ae")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-quantreg", type=("build", "run"))
	depends_on("r-sn", type=("build", "run"))
	depends_on("r-dfoptim", type=("build", "run"))
	depends_on("r-plot3d", type=("build", "run"))
