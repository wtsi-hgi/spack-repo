# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNextgenshinyapps(RPackage):
	"""Craft Exceptional 'R Shiny' Applications and Dashboards with
Novel Responsive Tools

	Nove responsive tools for designing and developing 'Shiny' dashboards and applications. The scripts and style sheets are based on 'jQuery' <https://jquery.com/> and 'Bootstrap' <https://getbootstrap.com/>.
	"""
	
	homepage = "https://nextgenshinyapps.obi.obianom.com"
	cran = "nextGenShinyApps" 

	version("2.0", md5="1a3f559eebcc9508c672d39612aad84a")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-quickcode", type=("build", "run"))
