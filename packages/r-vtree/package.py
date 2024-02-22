# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVtree(RPackage):
	"""Display Information About Nested Subsets of a Data Frame

	A tool for calculating and drawing "variable trees". Variable trees display information about nested subsets of a data frame.
	"""
	
	homepage = "https://github.com/nbarrowman/vtree"
	cran = "vtree" 

	version("5.6.5", md5="6b48e018ae8afdd0079a41874e17728e")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-diagrammer", type=("build", "run"))
	depends_on("r-diagrammersvg", type=("build", "run"))
	depends_on("r-rsvg", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-utf8", type=("build", "run"))
