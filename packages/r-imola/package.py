# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RImola(RPackage):
	"""CSS Layouts (Grid and Flexbox) Implementation for R/Shiny

	Allows easy creation of CSS layouts (grid and flexbox)
  directly from R without added CSS.
	"""
	
	homepage = "https://github.com/pedrocoutinhosilva/imola"
	cran = "imola" 

	version("0.5.0", md5="3676e0cd87c19c7cac234325e1151557")

	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
