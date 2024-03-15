# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSimhelpers(RPackage):
	"""Helper Functions for Simulation Studies

	Calculates performance criteria measures and associated Monte Carlo standard errors for simulation results. Includes functions to help run simulation studies. Our derivation and explanation of formulas and our general simulation workflow is closely aligned with the approach described by Morris, White, and Crowther (2019) <DOI:10.1002/sim.8086>. 
	"""
	
	homepage = "https://meghapsimatrix.github.io/simhelpers/index.html"
	cran = "simhelpers" 

	version("0.2.1", md5="841a08e179f4fd582306e19805de7300")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-furrr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-rstudioapi", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
