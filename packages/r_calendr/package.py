# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCalendr(RPackage):
	"""Ready to Print Monthly and Yearly Calendars Made with 'ggplot2'

	Contains the function calendR() for creating fully customizable monthly and yearly calendars (colors, fonts, formats, ...) and even heatmap calendars. In addition, it allows saving the calendars in ready to print A4 format PDF files.
	"""
	
	homepage = "https://r-coder.com/"
	cran = "calendR" 

	version("1.2", md5="bdfd426a19a9ccf24ae5d1d82a81faad")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
	depends_on("r-suncalc", type=("build", "run"))
	depends_on("r-ggimage", type=("build", "run"))
	depends_on("r-gggibbous", type=("build", "run"))
