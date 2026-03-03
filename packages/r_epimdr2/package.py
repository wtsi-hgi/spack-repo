# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REpimdr2(RPackage):
	"""Functions and Data for "Epidemics: Models and Data in R (2nd
Edition)"

	Functions, data sets and shiny apps for "Epidemics: Models and Data in R (2nd edition)" by Ottar N. Bjornstad (2022, ISBN: 978-3-031-12055-8) <https://link.springer.com/book/10.1007/978-3-319-97487-3>. The package contains functions to study the Susceptible-Exposed-Infected-Removed SEIR model, spatial and age-structured Susceptible-Infected-Removed SIR models; time-series SIR and chain-binomial stochastic models; catalytic disease models; coupled map lattice models of spatial transmission and network models for social spread of infection. The package is also an advanced quantitative companion to the 'Coursera' Epidemics Massive Online Open Course <https://www.coursera.org/learn/epidemics>.
	"""
	
	homepage = "<https://github.com/objornstad/epimdr2>"
	cran = "epimdr2" 

	version("1.0-9", md5="d9d710cd92d58b2bda5dabd697cf6ece", url="https://cran.r-project.org/src/contrib/epimdr2_1.0-9.tar.gz")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-desolve", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-polspline", type=("build", "run"))
	depends_on("r-phaser", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
