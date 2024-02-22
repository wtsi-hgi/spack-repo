# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpecies(RPackage):
	"""Statistical Package for Species Richness Estimation

	Implementation of various methods in estimation of species richness or diversity in Wang (2011)<doi:10.18637/jss.v040.i09>.
	"""
	
	cran = "SPECIES" 

	version("1.1.4", md5="6a267f8dcf705dce05585a14bdee6616")

