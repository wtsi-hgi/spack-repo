# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPopulation(RPackage):
	"""Models for Simulating Populations

	Run population simulations using an Individual-Based Model (IBM) compiled in C.
	"""
	
	cran = "population" 

	version("0.3", md5="f4dce8e134e9578ddcdc1e907280c370")

	depends_on("r-abind", type=("build", "run"))
