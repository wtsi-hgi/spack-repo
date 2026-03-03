# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDoremi(RPackage):
	"""Dynamics of Return to Equilibrium During Multiple Inputs

	Provides models to fit the dynamics of a regulated system experiencing exogenous inputs. 
    The underlying models use differential equations and linear mixed-effects regressions to estimate the 
    coefficients of the equation. With them, the functions can provide an estimated signal.
    The package provides simulation and analysis functions and also print, summary, plot and predict methods,
    adapted to the function outputs, for easy implementation and presentation of results.
	"""
	
	homepage = "https://github.com/dcourvoisier/doremi"
	cran = "doremi" 

	version("1.0.0", md5="0ed290d62321fbcb856ca5c6abb3744d")

	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-lmertest", type=("build", "run"))
	depends_on("r-desolve", type=("build", "run"))
	depends_on("r-futile-logger", type=("build", "run"))
