# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGginnards(RPackage):
	"""Explore the Innards of 'ggplot2' Objects

	Extensions to 'ggplot2' providing low-level debug tools: statistics
    and geometries echoing their data argument. Layer manipulation: deletion,
    insertion, extraction and reordering of layers. Deletion of unused variables
    from the data object embedded in "ggplot" objects.
	"""
	
	homepage = "https://www.r4photobiology.info"
	cran = "gginnards" 

	version("0.1.2", md5="c72d8eb996821ef71e074bde916ba574")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-ggplot2@3.3.1:", type=("build", "run"))
	depends_on("r-rlang@0.4:", type=("build", "run"))
	depends_on("r-stringr@1.4:", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-tibble@2.1:", type=("build", "run"))
