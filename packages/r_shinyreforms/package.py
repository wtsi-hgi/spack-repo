# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RShinyreforms(RPackage):
	"""Add Forms to your 'Shiny' App

	Allows to create modular, reusable 'HTML'
    forms which can be embedded in your 'shiny' app with minimal effort.
    Features include conditional code execution on form submission,
    automatic input validation and input tooltips.
	"""
	
	homepage = "https://github.com/piotrbajger/shinyreforms"
	cran = "shinyreforms" 

	version("0.0.1", md5="fce8fb3f901a9820459edd4aa24970f9")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-shiny@1:", type=("build", "run"))
	depends_on("r-htmltools@0.2.6:", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
