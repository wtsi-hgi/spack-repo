# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCoordinatecleaner(RPackage):
	"""Automated Cleaning of Occurrence Records from Biological
Collections

	Automated flagging of common spatial and temporal
    errors in biological and paleontological collection data, for the use
    in conservation, ecology and paleontology. Includes automated tests to
    easily flag (and exclude) records assigned to country or province
    centroid, the open ocean, the headquarters of the Global Biodiversity
    Information Facility, urban areas or the location of biodiversity
    institutions (museums, zoos, botanical gardens, universities).
    Furthermore identifies per species outlier coordinates, zero
    coordinates, identical latitude/longitude and invalid coordinates.
    Also implements an algorithm to identify data sets with a significant
    proportion of rounded coordinates. Especially suited for large data
    sets. The reference for the methodology is: Zizka et al. (2019)
    <doi:10.1111/2041-210X.13152>.
	"""
	
	homepage = "https://ropensci.github.io/CoordinateCleaner/"
	cran = "CoordinateCleaner" 

	version("3.0.1", md5="938c52401b1f65ef0d70e1489612d319")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-geosphere", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rgbif", type=("build", "run"))
	depends_on("r-rnaturalearth@0.3.2:", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("gdal@2.0.1:", type=("build", "link", "run"))
