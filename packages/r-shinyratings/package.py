# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RShinyratings(RPackage):
	"""An Intuitive Way of Providing Star Rating in a 'shiny' App

	A simple interface to integrate star ratings into your 'shiny' apps. 
            It can be used for customer feedback systems, user reviews, or any application that requires user ratings. 
            'shinyRatings' offers a straightforward and customisable solution that enhances user engagement and facilitates valuable feedback collection.
	"""
	
	cran = "shinyRatings" 

	version("0.1.0", md5="9a23dc506ca00adbb6704de2e61ce1ea")

	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
