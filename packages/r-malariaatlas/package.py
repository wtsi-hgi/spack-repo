# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMalariaatlas(RPackage):
	"""An R Interface to Open-Access Malaria Data, Hosted by the
'Malaria Atlas Project'

	A suite of tools to allow you to download all 
  publicly available parasite rate survey points, mosquito occurrence points and raster surfaces from 
  the 'Malaria Atlas Project' <https://malariaatlas.org/> servers as well as utility functions for plotting
  the downloaded data.
	"""
	
	homepage = "https://github.com/malaria-atlas-project/malariaAtlas"
	cran = "malariaAtlas" 

	version("1.5.1", md5="e0c39a31440774be144a31cce90236ef")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
	depends_on("r-tidyterra", type=("build", "run"))
	depends_on("r-ows4r", type=("build", "run"))
	depends_on("r-future-apply", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
