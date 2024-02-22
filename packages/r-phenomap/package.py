# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPhenomap(RPackage):
	"""Projecting Satellite-Derived Phenology in Space

	This takes in a series of multi-layer raster files and returns a phenology projection raster, following methodologies described in John (2016) <https://etda.libraries.psu.edu/catalog/13521clj5135>.
	"""
	
	homepage = "https://github.com/JepsonNomad/phenomap"
	cran = "phenomap" 

	version("2.0.1", md5="42814d92e68d09cd6e14ae6d55d9f579")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-phenex", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
