# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPolicyportfolios(RPackage):
	"""Tools for Managing, Measuring and Visualizing Policy Portfolios

	Tools for simplifying the creation and management of data structures
    suitable for dealing with policy portfolios, that is, two-dimensional spaces 
    of policy instruments and policy targets. The package also allows to generate measures of
    portfolio characteristics and facilitates their visualization.
	"""
	
	homepage = "http://xavier-fim.net/packages/PolicyPortfolios/"
	cran = "PolicyPortfolios" 

	version("0.3", md5="c9a7042bc43241d9a3c14e8ea3c0be50")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-vegan", type=("build", "run"))
	depends_on("r-ineq", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
