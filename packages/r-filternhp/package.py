# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFilternhp(RPackage):
	"""Non-Human Primate Search Filters

	Generate search filters to query scientific bibliographic sources, 
    such as PubMed and Web of Science, for non-human primate related 
    publications. 
	"""
	
	cran = "filterNHP" 

	version("0.1.2", md5="3994494fa247a0f0ab62fc7f8522c5c1")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-data-tree@1:", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinywidgets", type=("build", "run"))
	depends_on("r-shinyjs", type=("build", "run"))
	depends_on("r-shinybs", type=("build", "run"))
	depends_on("r-rclipboard", type=("build", "run"))
