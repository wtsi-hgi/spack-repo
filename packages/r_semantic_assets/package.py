# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSemanticAssets(RPackage):
	"""Assets for 'shiny.semantic'

	Style sheets and JavaScript assets for 'shiny.semantic' package.
	"""
	
	homepage = "https://github.com/Appsilon/semantic.assets"
	cran = "semantic.assets" 

	version("1.1.0", md5="3703b2bee9ef04846bb6566d623469ef")

	depends_on("r-htmlwidgets", type=("build", "run"))
