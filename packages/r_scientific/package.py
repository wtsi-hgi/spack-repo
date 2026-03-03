# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScientific(RPackage):
	"""Elegant Scientific Themed Reporting for 'Markdown'

	Offers 'markdown' output formats designed with various scientific styles, allowing users to generate PDF and HTML outputs. The output has a contemporary appearance with vibrant visuals, providing numerous styles for effective highlighting. The package also includes additional features specifically tailored for front-page slides, enhancing the overall presentation and customization options. The package was created using the 'tufte' <https://rstudio.github.io/tufte/> package code as a starting point.
	"""
	
	homepage = "https://scientific.obi.obianom.com"
	cran = "scientific" 

	version("2024.1", md5="b9a0c79be951e5ff20aa6a6bbcf6ff32")

	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-xfun", type=("build", "run"))
