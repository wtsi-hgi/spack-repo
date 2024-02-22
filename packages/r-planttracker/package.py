# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPlanttracker(RPackage):
	"""Extract Demographic and Competition Data from Fine-Scale Maps

	Extracts growth, survival, and local neighborhood density 
  information from repeated, fine-scale maps of organism occurrence. Further 
  information about this package can be found in our journal article, 
  "plantTracker: An R package to translate maps of plant occurrence into 
  demographic data" published in 2022 in Methods in Ecology and Evolution 
  (Stears, et al., 2022) <doi:10.1111/2041-210X.13950>. 
	"""
	
	homepage = "https://github.com/aestears/plantTracker"
	cran = "plantTracker" 

	version("1.1.0", md5="8e2c24aef71050f9e40d97c27ed283ee")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-units", type=("build", "run"))
