# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGators(RPackage):
	"""Geographic and Taxonomic Occurrence R-Based Scrubbing

	Streamlines downloading and cleaning biodiversity data from Integrated Digitized Biocollections (iDigBio) and the Global Biodiversity Information Facility (GBIF).
	"""
	
	homepage = "https://nataliepatten.github.io/gatoRs/"
	cran = "gatoRs" 

	version("1.0.1", md5="de05afb84cb4c2dc3288b4a92f35fc3f")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ridigbio", type=("build", "run"))
	depends_on("r-dplyr@1.1:", type=("build", "run"))
	depends_on("r-rgbif", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-coordinatecleaner@3.0.1:", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
	depends_on("r-spthin", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-leaflet", type=("build", "run"))
	depends_on("r-parsedate", type=("build", "run"))
	depends_on("r-spatstat-geom", type=("build", "run"))
