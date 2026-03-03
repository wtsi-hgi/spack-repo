# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RShinyFluent(RPackage):
	"""Microsoft Fluent UI for Shiny Apps

	
  A rich set of UI components for building Shiny applications,
  including inputs, containers, overlays, menus, and various utilities.
  All components from Fluent UI (the underlying JavaScript library)
  are available and have usage examples in R.
	"""
	
	homepage = "https://appsilon.github.io/shiny.fluent/"
	cran = "shiny.fluent" 

	version("0.3.0", md5="4955f75a9e75f69bab060fd9ba873ceb")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shiny-react@0.3:", type=("build", "run"))
