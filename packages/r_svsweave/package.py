# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSvsweave(RPackage):
	"""'SciViews' - 'Sweave', 'Knitr' and R Markdown Companion
Functions

	Functions to enumerate and reference figures, tables and equations
  in R Markdown documents that do not support these features (thus not
  'bookdown' or 'quarto'. Supporting functions for using 'Sweave' and 'Knitr'
  with 'LyX'. 
	"""
	
	homepage = "https://github.com/SciViews/svSweave"
	cran = "svSweave" 

	version("1.0.0", md5="1ec28c6a712d5522bf4045feb900bcb0")

	depends_on("r@2.6:", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
