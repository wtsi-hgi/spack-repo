# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDamaoi(RPackage):
	"""Create an 'Area of Interest' Around a Constructed Dam for
Comparative Impact Evaluations

	Define a spatial 'Area of Interest' (AOI) around a constructed dam using hydrology data.
  Dams have environmental and social impacts, both positive and negative.
  Current analyses of dams have no consistent way to specify at what spatial extent we should evaluate these impacts.
  'damAOI' implements methods to adjust reservoir polygons to match satellite-observed surface water areas, plot upstream and downstream rivers using elevation data and accumulated river flow, and draw buffers clipped by river basins around reservoirs and relevant rivers. 
  This helps to consistently determine the areas which could be impacted by dam construction, facilitating comparative analysis and informed infrastructure investments.
	"""
	
	cran = "damAOI" 

	version("0.0", md5="6de7e3efc3e14fe1d01f47d7456b3097")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-fnn", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-units", type=("build", "run"))
	depends_on("r-smoothr", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-leaflet", type=("build", "run"))
	depends_on("r-shinydashboard", type=("build", "run"))
