# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RShinyirt(RPackage):
	"""Item Response Theory Analysis with a 'shiny' Application

	Performing Item Response Theory analysis such as parameter estimation, ability estimation, item and model fit analyse, local independence assumption, dimensionality assumption, characteristic and information curves under various models with a user friendly 'shiny' interface.
	"""
	
	cran = "shinyIRT" 

	version("0.1", md5="453592a02f90224a3fde5e237593da9e")

	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinydashboard", type=("build", "run"))
	depends_on("r-shinycssloaders", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-mirt", type=("build", "run"))
	depends_on("r-psych", type=("build", "run"))
	depends_on("r-irtoys", type=("build", "run"))
