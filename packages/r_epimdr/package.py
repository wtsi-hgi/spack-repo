# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REpimdr(RPackage):
	"""Functions and Data for "Epidemics: Models and Data in R"

	Functions, data sets and shiny apps for "Epidemics: Models and Data in R" by Ottar N. Bjornstad (ISBN 978-3-319-97487-3) <https://www.springer.com/gp/book/9783319974866>. The package contains functions to study the S(E)IR model, spatial and age-structured SIR models; time-series SIR and chain-binomial stochastic models; catalytic disease models; coupled map lattice models of spatial transmission and network models for social spread of infection. The package is also an advanced quantitative companion to the coursera Epidemics Massive Online Open Course <https://www.coursera.org/learn/epidemics>.
	"""
	
	homepage = "https://github.com/objornstad/epimdr"
	cran = "epimdr" 

	version("0.6-5", md5="cf59de02138e83729be060cefd42bacb")

	depends_on("r@3.3.2:", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-desolve", type=("build", "run"))
	depends_on("r-polspline", type=("build", "run"))
