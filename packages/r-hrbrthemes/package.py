# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHrbrthemes(RPackage):
	"""Additional Themes, Theme Components and Utilities for 'ggplot2'

	A compilation of extra 'ggplot2' themes, scales and utilities, including a 
    spell check function for plot label fields and an overall emphasis on typography. 
    A copy of the 'Google' font 'Roboto Condensed' is also included.
	"""
	
	cran = "hrbrthemes" 

	version("0.8.7", md5="2c239ee48ed2bf410b7e99f8c746c7ef")
	version("0.8.0", md5="164d952f9627188cff499edd1cce9c5c")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-ggplot2@3.4:", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-extrafont", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-gdtools", type=("build", "run"))
