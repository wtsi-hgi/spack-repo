# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNatTemplatebrains(RPackage):
	"""NeuroAnatomy Toolbox ('nat') Extension for Handling Template
Brains

	Extends package 'nat' (NeuroAnatomy Toolbox) by
    providing objects and functions for handling template brains.
	"""
	
	homepage = "http://natverse.org/nat.templatebrains/"
	cran = "nat.templatebrains" 

	version("1.1", md5="9549180fd139f27413b09e7872fc64bc")

	depends_on("r-nat@1.8.6:", type=("build", "run"))
	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rgl", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-memoise", type=("build", "run"))
	depends_on("r-rappdirs", type=("build", "run"))
	depends_on("r-morpho", type=("build", "run"))
