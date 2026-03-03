# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RShinyPwa(RPackage):
	"""Progressive Web App Support for Shiny

	Adds Progressive Web App support for Shiny apps, including
  desktop and mobile installations.
	"""
	
	homepage = "https://github.com/pedrocoutinhosilva/shiny.pwa"
	cran = "shiny.pwa" 

	version("0.2.1", md5="db8f6d8a87bd91ed8c3e0a9007faffa4")

	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-urltools", type=("build", "run"))
