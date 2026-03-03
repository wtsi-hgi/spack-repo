# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIbmcraftr(RPackage):
	"""Toolkits to Develop Individual-Based Models in Infectious
Disease

	It provides a generic set of tools for initializing a synthetic
         population with each individual in specific disease states, and
         making transitions between those disease states according to the rates
         calculated on each timestep. The new version 1.0.0 has C++ code 
         integration to make the functions run faster. It has also a higher level
         function to actually run the transitions for the number of timesteps
         that users specify. Additional functions will follow for changing
         attributes on demographic, health belief and movement.
	"""
	
	cran = "ibmcraftr" 

	version("1.0.0", md5="c6d6948c38caf4af6139d7bea4e3a3b7")

	depends_on("r-rcpp", type=("build", "run"))
