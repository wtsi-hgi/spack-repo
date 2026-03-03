# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIsocir(RPackage):
	"""Isotonic Inference for Circular Data

	A bunch of functions to deal with circular data under order restrictions.
	"""
	
	cran = "isocir" 

	version("2.0-7.1", md5="5583b35386134aa846c6d3ed1ebbdfbe")

	depends_on("r@3.0.1:", type=("build", "run"))
	depends_on("r-circular@0.4.8:", type=("build", "run"))
	depends_on("r-tsp@1.0.7:", type=("build", "run"))
	depends_on("r-combinat@0.0.8:", type=("build", "run"))
