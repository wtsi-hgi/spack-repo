# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNetindices(RPackage):
	"""Estimating Network Indices, Including Trophic Structure of
Foodwebs in R

	Given a network (e.g. a food web), estimates several network indices. These include: Ascendency network indices, Direct and indirect dependencies, Effective measures, Environ network indices, General network indices, Pathway analysis, Network uncertainty indices and constraint efficiencies and the trophic level and omnivory indices of food webs.
	"""
	
	cran = "NetIndices" 

	version("1.4.4.1", md5="234aeb6e3960dcdb74efdf01fbd1e790")

	depends_on("r@2.1:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
