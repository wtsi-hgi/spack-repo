# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIrtgui(RPackage):
	"""Item Response Theory Analysis with a Graphic User Interface

	Performing Item Response Theory analysis such as parameter estimation, ability estimation, data generation, item and model fit analyse, local independence assumption, dimensionality assumption, wright map, characteristic and information curves under various models with a user-friendly Graphic User Interface.
	"""
	
	cran = "irtGUI" 

	version("0.2", md5="7bd958094d9e2e27fc79a49bc44afab9")

	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinydashboard", type=("build", "run"))
	depends_on("r-shinycssloaders", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-mirt", type=("build", "run"))
	depends_on("r-psych", type=("build", "run"))
	depends_on("r-wrightmap", type=("build", "run"))
	depends_on("r-writexl", type=("build", "run"))
	depends_on("r-irtoys", type=("build", "run"))
