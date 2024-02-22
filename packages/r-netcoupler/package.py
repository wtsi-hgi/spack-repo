# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNetcoupler(RPackage):
	"""Inference of Causal Links Between a Network and an External
Variable

	The 'NetCoupler' algorithm identifies potential direct effects of 
    correlated, high-dimensional variables formed as a network with an external 
    variable. The external variable may act as the dependent/response variable 
    or as an independent/predictor variable to the network. 
	"""
	
	homepage = "https://github.com/NetCoupler/NetCoupler"
	cran = "NetCoupler" 

	version("0.1.0", md5="a1c19a29e2ca476eb9361b1ede13328e")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ids", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-pcalg", type=("build", "run"))
	depends_on("r-ppcor", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang@0.4.6:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-tidygraph", type=("build", "run"))
