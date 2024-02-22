# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REcospat(RPackage):
	"""Spatial Ecology Miscellaneous Methods

	Collection of R functions and data sets for the support of spatial ecology analyses with a focus on pre, core and post modelling analyses of species distribution, niche quantification and community assembly. Written by current and former members and collaborators of the ecospat group of Antoine Guisan, Department of Ecology and Evolution (DEE) and Institute of Earth Surface Dynamics (IDYST), University of Lausanne, Switzerland. Read Di Cola et al. (2016) <doi:10.1111/ecog.02671> for details.
	"""
	
	homepage = "http://www.unil.ch/ecospat/home/menuguid/ecospat-resources/tools.html"
	cran = "ecospat" 

	version("4.0.0", md5="f5aa3fcf2db56a8b62d29cbb43fe682b")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-ade4@1.6.2:", type=("build", "run"))
	depends_on("r-gbm@2.1.1:", type=("build", "run"))
	depends_on("r-foreach@1.4.3:", type=("build", "run"))
	depends_on("r-adehabitathr@0.4.11:", type=("build", "run"))
	depends_on("r-adehabitatma@0.3.8:", type=("build", "run"))
	depends_on("r-biomod2@4.2.3:", type=("build", "run"))
	depends_on("r-dismo@0.9.3:", type=("build", "run"))
	depends_on("r-ecodist@1.2.9:", type=("build", "run"))
	depends_on("r-terra@1.2.5:", type=("build", "run"))
	depends_on("r-gtools@3.4.1:", type=("build", "run"))
	depends_on("r-presenceabsence@1.1.9:", type=("build", "run"))
	depends_on("r-classint@0.1.23:", type=("build", "run"))
	depends_on("r-vegan@2.4.1:", type=("build", "run"))
	depends_on("r-poibin@1.3:", type=("build", "run"))
	depends_on("r-matrixstats@0.53.1:", type=("build", "run"))
	depends_on("r-ks@1.12:", type=("build", "run"))
	depends_on("r-nabor@0.5:", type=("build", "run"))
	depends_on("r-hmisc@4.4.2:", type=("build", "run"))
