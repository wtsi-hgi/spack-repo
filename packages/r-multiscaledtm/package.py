# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMultiscaledtm(RPackage):
	"""Multi-Scale Geomorphometric Terrain Attributes

	Calculates multi-scale geomorphometric terrain attributes from regularly gridded digital terrain models using a variable focal windows size (Ilich et al. (2023) <doi:10.1111/tgis.13067>).
	"""
	
	homepage = "https://ailich.github.io/MultiscaleDTM/"
	cran = "MultiscaleDTM" 

	version("0.8.3", md5="b8ef5fa29903a0bbb60135d9a1e8f68e")

	depends_on("r-terra@1.7.46:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-rgl", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
