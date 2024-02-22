# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSoilassessment(RPackage):
	"""Assessment Models for Agriculture Soil Conditions and Crop
Suitability

	Soil assessment builds information for improved decision in
    soil management. It analyzes soil conditions with regard to
    agriculture crop suitability requirements [such as those given by FAO
    <https://www.fao.org/land-water/databases-and-software/crop-information/en/>]
    soil fertility classes, soil erosion, and soil salinity classification
    [<doi:10.1002/ldr.4211>]. Suitability requirements are for
    crops grouped into cereal crops, nuts, legumes, fruits, vegetables,
    industrial crops, and root crops.
	"""
	
	cran = "soilassessment" 

	version("0.2.6", md5="4f211c674f276dbc6f8364b2bd1cfa7c")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
	depends_on("r-desolve", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-fuzzyahp", type=("build", "run"))
	depends_on("r-googledrive", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
	depends_on("r-nnet", type=("build", "run"))
	depends_on("r-png", type=("build", "run"))
	depends_on("r-randomforest", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r-soiltexture", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
