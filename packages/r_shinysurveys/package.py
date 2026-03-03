# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RShinysurveys(RPackage):
	"""Create and Deploy Surveys in 'Shiny'

	Easily create and deploy surveys in 'Shiny'. This package includes
    a minimalistic framework similar to 'Google Forms' that allows for url-based
    user tracking, customizable submit actions, easy survey-theming, and more.
	"""
	
	cran = "shinysurveys" 

	version("0.2.0", md5="097db8267121910681ed18d9a4f0a545")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-sass", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
