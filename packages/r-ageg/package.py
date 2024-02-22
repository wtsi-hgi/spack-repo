# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAgeg(RPackage):
	"""Age Grouping Functions

	Pair of simple convenience functions to convert a vector of birth dates to age and age distributions. These functions may be helpful when related age and custom age distributions are desired given a vector of birth dates.
	"""
	
	cran = "ageg" 

	version("1.0.0", md5="44a75ed9b652b3fb9a2aa3e6d19ab874")

