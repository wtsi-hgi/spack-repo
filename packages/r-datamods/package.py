# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDatamods(RPackage):
	"""Modules to Import and Manipulate Data in 'Shiny'

	'Shiny' modules to import data into an application or 'addin'
    from various sources, and to manipulate them after that.
	"""
	
	homepage = "https://github.com/dreamRs/datamods"
	cran = "datamods" 

	version("1.4.5", md5="44613cd3724dda42cafb4364c4aebd00")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-phosphoricons", type=("build", "run"))
	depends_on("r-reactable", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-rio", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-shiny@1.5:", type=("build", "run"))
	depends_on("r-shinywidgets@0.7.3:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-shinybusy", type=("build", "run"))
	depends_on("r-writexl", type=("build", "run"))
