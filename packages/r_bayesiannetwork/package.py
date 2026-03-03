# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBayesiannetwork(RPackage):
	"""Bayesian Network Modeling and Analysis

	A "Shiny"" web application for creating interactive Bayesian Network models,
    learning the structure and parameters of Bayesian networks, and utilities for classic
    network analysis.
	"""
	
	homepage = "https://github.com/paulgovan/bayesiannetwork"
	cran = "BayesianNetwork" 

	version("0.3", md5="362a574ca377683c05638eeaca6ed8e6")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-bnlearn", type=("build", "run"))
	depends_on("r-heatmaply", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-networkd3", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-rintrojs", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinyace", type=("build", "run"))
	depends_on("r-shinydashboard", type=("build", "run"))
	depends_on("r-shinywidgets", type=("build", "run"))
