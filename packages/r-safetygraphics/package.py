# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSafetygraphics(RPackage):
	"""Interactive Graphics for Monitoring Clinical Trial Safety

	A framework for evaluation of clinical trial safety. Users can interactively explore their data using the included 'Shiny' application. 
	"""
	
	homepage = "https://github.com/SafetyGraphics/safetyGraphics"
	cran = "safetyGraphics" 

	version("2.1.1", md5="ddf9753f77155e54eb79707dab7df477")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-dt@0.19:", type=("build", "run"))
	depends_on("r-datamods@1.1.5:", type=("build", "run"))
	depends_on("r-htmlwidgets@1.5:", type=("build", "run"))
	depends_on("r-jsonlite@1.7:", type=("build", "run"))
	depends_on("r-magrittr@2:", type=("build", "run"))
	depends_on("r-purrr@0.3:", type=("build", "run"))
	depends_on("r-rclipboard@0.1.3:", type=("build", "run"))
	depends_on("r-rlang@0.4.11:", type=("build", "run"))
	depends_on("r-safetydata@1:", type=("build", "run"))
	depends_on("r-safetycharts@0.3:", type=("build", "run"))
	depends_on("r-shiny@1.6:", type=("build", "run"))
	depends_on("r-shinyjs@2:", type=("build", "run"))
	depends_on("r-sortable@0.4.4:", type=("build", "run"))
	depends_on("r-stringr@1.4:", type=("build", "run"))
	depends_on("r-tidyr@1.2:", type=("build", "run"))
	depends_on("r-yaml@2.2.1:", type=("build", "run"))
