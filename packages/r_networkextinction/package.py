# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNetworkextinction(RPackage):
	"""Extinction Simulation in Ecological Networks

	Simulates the extinction of species in ecological networks and it analyzes
             its cascading effects, described in Dunne et al. (2002) <doi:10.1073/pnas.192407699>.
	"""
	
	homepage = "https://derek-corcoran-barrios.github.io/NetworkExtinction/"
	cran = "NetworkExtinction" 

	version("1.0.3", md5="cac6daeac7395907b442af9221b84e10")

	depends_on("r@3.5.1:", type=("build", "run"))
	depends_on("r-broom", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-network", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-sna", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-patchwork", type=("build", "run"))
	depends_on("r-dosnow", type=("build", "run"))
