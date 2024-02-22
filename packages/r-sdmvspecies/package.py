# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSdmvspecies(RPackage):
	"""Create Virtual Species for Species Distribution Modelling

	A software package help user to create virtual species for species distribution modelling. It includes
    several methods to help user to create virtual species distribution map.
    Those maps can be used for Species Distribution Modelling (SDM) study. SDM use
    environmental data for sites of occurrence of a species to predict all the sites
    where the environmental conditions are suitable for the species to persist, and
    may be expected to occur.
	"""
	
	homepage = "http://www.sdmserialsoftware.org/sdmvspecies/"
	cran = "sdmvspecies" 

	version("0.3.2", md5="777dc870c85c87cbf395d4c9cc2a32a3")

	depends_on("r-raster", type=("build", "run"))
	depends_on("r-psych", type=("build", "run"))
