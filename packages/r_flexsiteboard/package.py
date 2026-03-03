# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFlexsiteboard(RPackage):
	"""Breaks Single Page Applications from 'flexdashboard' in Multiple
Files

	A drop-in replacement for 'flexdashboard' 'Rmd' documents, which
  implements an after-knit-hook to split the generated single page application
  in one document per main section to reduce rendering load in the web browser
  displaying the document. Put all 'JavaScript' stuff needed in all sections 
  before the first headline featuring navigation menu attributes. This package 
  is experimental and maybe replaced by a solution inside 'flexdashboard'.
	"""
	
	homepage = "https://gitlab.com/libreumg/flexsiteboard/"
	cran = "flexsiteboard" 

	version("0.0.7", md5="87f6610d51f09ba7107db5216058f658")

	depends_on("r-flexdashboard", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
	depends_on("pandoc@2.4:", type=("build", "link", "run"))
