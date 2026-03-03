# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDartrSpatial(RPackage):
	"""Applying Landscape Genomic Methods on 'SNP' and 'Silicodart'
Data

	Provides landscape genomic functions to analyse 'SNP' (single nuclear
    polymorphism) data, such as least cost path analysis and isolation by distance. 
    Therefore each sample needs to have coordinate data attached (lat/lon) to be 
    able to run most of the functions. 'dartR.spatial' is a package that belongs
    to the 'dartRverse' suit of packages and depends on 'dartR.base' and 'dartR.data'.
	"""
	
	homepage = "https://green-striped-gecko.github.io/dartR/"
	cran = "dartR.spatial" 

	version("0.78", md5="2cb915401d840fe7cf69111edbae202d")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-adegenet@2:", type=("build", "run"))
	depends_on("r-dartr-base", type=("build", "run"))
	depends_on("r-dartr-data", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-stampp", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-vegan", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
