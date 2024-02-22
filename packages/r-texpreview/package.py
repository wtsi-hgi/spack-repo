# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTexpreview(RPackage):
	"""Compile and Preview Snippets of 'LaTeX'

	Compile snippets of 'LaTeX' directly into images
    from the R console to view in the 'RStudio' viewer pane, Shiny apps
    and 'RMarkdown' documents.
	"""
	
	homepage = "https://github.com/yonicd/texPreview"
	cran = "texPreview" 

	version("2.1.0", md5="aca25be57931d12b68a3f0934ce11c37")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-base64enc", type=("build", "run"))
	depends_on("r-details", type=("build", "run"))
	depends_on("r-fs", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-magick", type=("build", "run"))
	depends_on("r-rematch2", type=("build", "run"))
	depends_on("r-rstudioapi", type=("build", "run"))
	depends_on("r-svgpanzoom", type=("build", "run"))
	depends_on("r-whisker", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-tinytex", type=("build", "run"))
