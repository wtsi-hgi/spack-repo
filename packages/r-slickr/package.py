# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSlickr(RPackage):
	"""Create Interactive Carousels with the 'JavaScript' 'Slick'
Library

	Create and customize interactive carousels
      using the 'Slick' 'JavaScript' library and the
      'htmlwidgets' package. The carousels can contain
      plots produced in R, images, 'iframes', videos and
      other 'htmlwidgets'.  These carousels can be created
      directly from the R console, and viewed in the 'RStudio' 
      internal viewer, in 'Shiny' apps and R Markdown documents.
	"""
	
	homepage = "https://github.com/yonicd/slickR"
	cran = "slickR" 

	version("0.6.0", md5="9c578c2d127b9d923af810f4cec75a63")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-base64enc", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
