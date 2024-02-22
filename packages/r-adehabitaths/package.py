# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAdehabitaths(RPackage):
	"""Analysis of Habitat Selection by Animals

	A collection of tools for the analysis of habitat selection.
	"""
	
	cran = "adehabitatHS" 

	version("0.3.17", md5="bfc8fe296f18b7208082ce7c293ed4ef")

	depends_on("r@3.0.1:", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-ade4", type=("build", "run"))
	depends_on("r-adehabitatma", type=("build", "run"))
	depends_on("r-adehabitathr", type=("build", "run"))
