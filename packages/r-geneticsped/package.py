# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGeneticsped(RPackage):
	"""Pedigree and genetic relationship functions

	Classes and methods for handling pedigree data. It also includes functions to calculate genetic relationship measures as relationship and inbreeding coefficients and other utilities. Note that package is not yet stable. Use it with care!
	"""
	
	homepage = "http://rgenetics.org"
	bioc = "GeneticsPed"

	version("1.70.0", commit="340bd0d74c563d4415354bef97aac7e8ff62294c")
	version("1.64.0", commit="37359e5743a1e7c31af85e8525c68c2e5dd7eb23")

	depends_on("r@2.4:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-gdata", type=("build", "run"))
	depends_on("r-genetics", type=("build", "run"))
