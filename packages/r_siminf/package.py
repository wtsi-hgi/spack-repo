# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSiminf(RPackage):
	"""A Framework for Data-Driven Stochastic Disease Spread
Simulations

	Provides an efficient and very flexible framework to
    conduct data-driven epidemiological modeling in realistic large
    scale disease spread simulations. The framework integrates
    infection dynamics in subpopulations as continuous-time Markov
    chains using the Gillespie stochastic simulation algorithm and
    incorporates available data such as births, deaths and movements
    as scheduled events at predefined time-points. Using C code for
    the numerical solvers and 'OpenMP' (if available) to divide work
    over multiple processors ensures high performance when simulating
    a sample outcome. One of our design goals was to make the package
    extendable and enable usage of the numerical solvers from other R
    extension packages in order to facilitate complex epidemiological
    research. The package contains template models and can be extended
    with user-defined models. For more details see the paper by
    Widgren, Bauer, Eriksson and Engblom (2019)
    <doi:10.18637/jss.v091.i12>. The package also provides
    functionality to fit models to time series data using the
    Approximate Bayesian Computation Sequential Monte Carlo
    ('ABC-SMC') algorithm of Toni and others (2009)
    <doi:10.1098/rsif.2008.0172>.
	"""
	
	homepage = "https://github.com/stewid/SimInf"
	cran = "SimInf" 

	version("9.6.0", md5="0f39a66c1f180d7c3a12ddb67759e4a3")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-matrix@1.3.0:", type=("build", "run"))
	depends_on("gsl", type=("build", "link", "run"))
