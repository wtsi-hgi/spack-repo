# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RShinysir(RPackage):
	"""Interactive Plotting for Mathematical Models of Infectious
Disease Spread

	Provides interactive plotting for mathematical models of infectious disease spread. Users can choose from a variety of common built-in ordinary differential equation (ODE) models (such as the SIR, SIRS, and SIS models), or create their own. This latter flexibility allows 'shinySIR' to be applied to simple ODEs from any discipline. The package is a useful teaching tool as students can visualize how changing different parameters can impact model dynamics, with minimal knowledge of coding in R. The built-in models are inspired by those featured in Keeling and Rohani (2008) <doi:10.2307/j.ctvcm4gk0> and Bjornstad (2018) <doi:10.1007/978-3-319-97487-3>.
	"""
	
	cran = "shinySIR" 

	version("0.1.2", md5="3736d8cdc06fc2b312a3375c05b54013")

	depends_on("r-dplyr@0.8.0.1:", type=("build", "run"))
	depends_on("r-tidyr@0.8.3:", type=("build", "run"))
	depends_on("r-ggplot2@3.1.1:", type=("build", "run"))
	depends_on("r-shiny@1.3.2:", type=("build", "run"))
	depends_on("r-desolve@1.2.1:", type=("build", "run"))
