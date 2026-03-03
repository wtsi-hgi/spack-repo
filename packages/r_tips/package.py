# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTips(RPackage):
	"""Trajectories and Phylogenies Simulator

	Generates stochastic time series and genealogies associated with a population dynamics model. Times series are simulated using the Gillespie exact and approximate algorithms and a new algorithm we introduce that uses both approaches to optimize the time execution of the simulations. Genealogies are simulated from a trajectory using a backwards-in-time based approach. Methods are described in Danesh G et al (2022) <doi:10.1111/2041-210X.14038>.
	"""
	
	homepage = "https://gitlab.in2p3.fr/ete/tips/"
	cran = "TiPS" 

	version("1.2.3", md5="9d2311a1bcd2ff57f20bd5e8ba0fdeac")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-inline", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
