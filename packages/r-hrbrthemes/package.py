# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHrbrthemes(RPackage):
	"""Additional Themes, Theme Components and Utilities for 'ggplot2'

	A compilation of extra 'ggplot2' themes, scales and utilities, including a 
    spell check function for plot label fields and an overall emphasis on typography. 
    A copy of the 'Google' font 'Roboto Condensed' <https://github.com/google/roboto/> 
    is also included along with a copy of the 'IBM' 'Plex Sans' <https://github.com/IBM/type>,
    'Titillium Web' <https://fonts.google.com/specimen/Titillium+Web>, and
    'Public Sans' <https://github.com/uswds/public-sans/> fonts
    are also included to support their respective typography-oriented themes.
	"""
	
	homepage = "http://github.com/hrbrmstr/hrbrthemes"
	cran = "hrbrthemes" 

	version("0.8.0", md5="164d952f9627188cff499edd1cce9c5c")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-ggplot2@3.3:", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-extrafont", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-gdtools", type=("build", "run"))
