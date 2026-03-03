# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REcochange(RPackage):
	"""Integrating Ecosystem Remote Sensing Products to Derive EBV
Indicators

	Essential Biodiversity Variables (EBV) are state variables with dimensions on time, space, and biological organization that document biodiversity change. Freely available ecosystem remote sensing products (ERSP) are downloaded and integrated with data for national or regional domains to derive indicators for EBV in the class ecosystem structure (Pereira et al., 2013) <doi:10.1126/science.1229931>, including horizontal ecosystem extents, fragmentation, and information-theory indices. To process ERSP, users must provide a polygon or geographic administrative data map. Downloadable ERSP include Global Surface Water (Peckel et al., 2016) <doi:10.1038/nature20584>, Forest Change (Hansen et al., 2013) <doi:10.1126/science.1244693>, and Continuous Tree Cover data (Sexton et al., 2013) <doi:10.1080/17538947.2013.786146>. 
	"""
	
	cran = "ecochange" 

	version("2.9.3.1", md5="cbe32830633b9263bd708247f9208663")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-rastervis", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-landscapemetrics", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-geodata", type=("build", "run"))
	depends_on("r-getpass", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-rasterdt", type=("build", "run"))
