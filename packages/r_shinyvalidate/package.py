# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RShinyvalidate(RPackage):
	"""Input Validation for Shiny Apps

	Improves the user experience of Shiny apps by helping to
    provide feedback when required inputs are missing, or input values
    are not valid.
	"""
	
	homepage = "https://rstudio.github.io/shinyvalidate/"
	cran = "shinyvalidate" 

	version("0.1.3", md5="c26281c4f35009b893898d07d71929cc")

	depends_on("r-shiny@1.6:", type=("build", "run"))
	depends_on("r-htmltools@0.5.1.1:", type=("build", "run"))
	depends_on("r-rlang@0.4.10:", type=("build", "run"))
	depends_on("r-glue@1.4.2:", type=("build", "run"))
