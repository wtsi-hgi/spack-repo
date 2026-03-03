# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RReactable(RPackage):
	"""Interactive Data Tables for R

	Interactive data tables for R, based on the 'React Table'
    JavaScript library. Provides an HTML widget that can be used in 'R Markdown'
    or 'Quarto' documents, 'Shiny' applications, or viewed from an R console.
	"""
	
	homepage = "https://glin.github.io/reactable/"
	cran = "reactable" 

	version("0.4.4", md5="b099ce6d92b9363226c1f4902f4a74b3")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-htmltools@0.5.2:", type=("build", "run"))
	depends_on("r-htmlwidgets@1.5.3:", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-reactr", type=("build", "run"))
