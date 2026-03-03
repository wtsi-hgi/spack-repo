# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClimind(RPackage):
	"""Climate Indices

	Computes 138 standard climate indices at monthly, seasonal and annual resolution. These indices were selected, based on their direct and significant impacts on target sectors, after a thorough review of the literature in the field of extreme weather events and natural hazards. Overall, the selected indices characterize different aspects of the frequency, intensity and duration of extreme events, and are derived from a broad set of climatic variables, including surface air temperature, precipitation, relative humidity, wind speed, cloudiness, solar radiation, and snow cover. The 138 indices have been classified as follow: Temperature based indices (42), Precipitation based indices (22), Bioclimatic indices (21), Wind-based indices (5), Aridity/ continentality indices (10), Snow-based indices (13), Cloud/radiation based indices (6), Drought indices (8), Fire indices (5), Tourism indices (5).
	"""
	
	homepage = "https://gitlab.com/indecis-eu/indecis"
	cran = "ClimInd" 

	version("0.1-3", md5="5670db86d6fb1f36f3f7b319de4e2ed3")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-spei", type=("build", "run"))
	depends_on("r-chron", type=("build", "run"))
	depends_on("r-weathermetrics", type=("build", "run"))
