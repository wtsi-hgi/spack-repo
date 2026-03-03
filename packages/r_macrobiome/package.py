# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMacrobiome(RPackage):
	"""A Tool for Mapping the Distribution of the Biomes and Bioclimate

	Procedures for simulating biomes by equilibrium vegetation 
  models, with a special focus on paleoenvironmental applications.
  Three widely used equilibrium biome models are currently implemented in 
  the package: the Holdridge Life Zone (HLZ) system (Holdridge 1947, 
  <doi:10.1126/science.105.2727.367>), the Köppen-Geiger classification 
  (KGC) system (Köppen 1936, 
  <https://koeppen-geiger.vu-wien.ac.at/pdf/Koppen_1936.pdf>) and the 
  BIOME model (Prentice et al. 1992, <doi:10.2307/2845499>). Three 
  climatic forest-steppe models are also implemented.
  An approach for estimating monthly time series of relative sunshine 
  duration from temperature and precipitation data (Yin 1999, 
  <doi:10.1007/s007040050111>) is also adapted, allowing 
  process-based biome models to be combined with high-resolution 
  paleoclimate simulation datasets (e.g., CHELSA-TraCE21k v1.0 dataset: 
  <https://chelsa-climate.org/chelsa-trace21k/>).
	"""
	
	homepage = "https://github.com/szelepcsenyi/macroBiome"
	cran = "macroBiome" 

	version("0.4.0", md5="a85bdee269c0d4fc108d485253660fe0")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-devtools", type=("build", "run"))
	depends_on("r-palinsol", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r-rnaturalearthdata", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-strex", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
