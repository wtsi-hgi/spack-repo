# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIsrad(RPackage):
	"""Tools and Data for the International Soil Radiocarbon Database

	This is the central location for data and tools for the development,
    maintenance, analysis, and deployment of the International Soil Radiocarbon Database
    (ISRaD). ISRaD was developed as a collaboration between the U.S. Geological Survey
    Powell Center and the Max Planck Institute for Biogeochemistry. This R package provides
    tools for accessing and manipulating ISRaD data, compiling local data using the ISRaD
    data structure, and simple query and reporting functions for ISRaD. For more detailed
    information visit the ISRaD website at: <https://soilradiocarbon.org/>.
	"""
	
	cran = "ISRaD" 

	version("2.5.5", md5="a2fa19f9c290140f863235c35aa6ac38")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-writexl", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
	depends_on("r-dplyr@0.8:", type=("build", "run"))
	depends_on("r-tidyr@1:", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-maps", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-rio", type=("build", "run"))
	depends_on("r-rnaturalearth", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
