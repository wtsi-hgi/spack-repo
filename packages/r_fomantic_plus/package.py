# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFomanticPlus(RPackage):
	"""Add Extra 'Fomantic UI' Components to 'shiny.semantic'

	Extend 'shiny.semantic' with extra 'Fomantic UI' components.
    Create pages in a format similar to 'shiny', form validation and more.
	"""
	
	homepage = "https://github.com/ashbaldry/fomantic.plus"
	cran = "fomantic.plus" 

	version("0.1.0", md5="a3d58a90689a002a813ab30f74711434")

	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shiny-semantic", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
