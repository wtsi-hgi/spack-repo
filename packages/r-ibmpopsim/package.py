# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIbmpopsim(RPackage):
	"""Individual Based Model Population Simulation

	Simulation of the random evolution of heterogeneous populations using stochastic Individual-Based Models (IBMs) <doi:10.48550/arXiv.2303.06183>. 
    The package enables users to simulate population evolution, in which individuals are characterized by their age and some characteristics, and the population is modified by different types of events, including births/arrivals, death/exit events, or changes of characteristics. The frequency at which an event can occur to an individual can depend on their age and characteristics, but also on the characteristics of other individuals (interactions). 
    Such models have a wide range of applications. For instance, IBMs can be used for simulating the evolution of a heterogeneous insurance portfolio with selection or for validating  mortality forecasts. 
    This package overcomes the limitations of time-consuming IBMs simulations by implementing new efficient algorithms  based on thinning methods, which are compiled using the 'Rcpp' package while providing a user-friendly interface.
	"""
	
	homepage = "https://github.com/DaphneGiorgi/IBMPopSim"
	cran = "IBMPopSim" 

	version("1.0.0", md5="c3c67d57245bf1ca12410c0b74fcadc6")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-dplyr@0.8:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
