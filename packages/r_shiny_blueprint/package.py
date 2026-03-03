# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RShinyBlueprint(RPackage):
	"""Palantir's 'Blueprint' for 'Shiny' Apps

	
  Easily use 'Blueprint', the popular 'React' library from Palantir, in your 'Shiny' app.
  'Blueprint' provides a rich set of UI components for creating visually appealing applications
  and is optimized for building complex, data-dense web interfaces.
  This package provides most components from the underlying library,
  as well as special wrappers for some components
  to make it easy to use them in 'R' without writing 'JavaScript' code.
	"""
	
	cran = "shiny.blueprint" 

	version("0.2.0", md5="ca9ae470ba234eae4d07f50bc8add2bd")

	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shiny-react@0.2.2:", type=("build", "run"))
