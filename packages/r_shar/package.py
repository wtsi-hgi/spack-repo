# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RShar(RPackage):
	"""Species-Habitat Associations

	
  Analyse species-habitat associations in R. Therefore, information about the location 
  of the species (as a point pattern) is needed together with environmental conditions 
  (as a categorical raster). To test for significance habitat associations, one of 
  the two components is randomized. Methods are mainly based on Plotkin et al. (2000) 
  <doi:10.1006/jtbi.2000.2158> and Harms et al. (2001) <doi:10.1111/j.1365-2745.2001.00615.x>.
	"""
	
	homepage = "https://r-spatialecology.github.io/shar/"
	cran = "shar" 

	version("2.3", md5="e1c154299ed686ffa65a63686754cc95")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-classint", type=("build", "run"))
	depends_on("r-spatstat-explore", type=("build", "run"))
	depends_on("r-spatstat-geom", type=("build", "run"))
	depends_on("r-spatstat-model", type=("build", "run"))
	depends_on("r-spatstat-random", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
