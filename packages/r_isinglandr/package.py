# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIsinglandr(RPackage):
	"""Landscape Construction and Simulation for Ising Networks

	A toolbox for constructing potential landscapes for Ising
    networks. The parameters of the networks can be directly supplied by
    users or estimated by the 'IsingFit' package by van Borkulo and
    Epskamp (2016) <https://CRAN.R-project.org/package=IsingFit> from
    empirical data. The Ising model's Boltzmann distribution is preserved
    for the potential landscape function. The landscape functions can be
    used for quantifying and visualizing the stability of network states,
    as well as visualizing the simulation process.
	"""
	
	homepage = "https://sciurus365.github.io/Isinglandr/"
	cran = "Isinglandr" 

	version("0.1.1", md5="ee4c9d79327152f7b40536bbdeb7cb99")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-gganimate", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinycssloaders", type=("build", "run"))
	depends_on("r-shinythemes", type=("build", "run"))
	depends_on("r-simlandr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
