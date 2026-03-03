# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMarkdowninput(RPackage):
	"""Shiny Module for a Markdown Input with Result Preview

	An R-Shiny module containing a "markdownInput". This input allows
    the user to write some markdown code and to preview the result. This input
    has been inspired by the "comment" window of <https://github.com/>.
	"""
	
	homepage = "https://github.com/juliendiot42/markdownInput"
	cran = "markdownInput" 

	version("0.1.2", md5="58828e4e885e108446920086cdd744a3")

	depends_on("r-shiny@1.0.5:", type=("build", "run"))
	depends_on("r-shinyace", type=("build", "run"))
	depends_on("r-markdown", type=("build", "run"))
