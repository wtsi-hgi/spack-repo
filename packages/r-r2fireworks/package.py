# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RR2fireworks(RPackage):
	"""Enhance Your 'Rmarkdown' and 'shiny' Apps with Dazzling
Fireworks Celebrations

	Implementation of 'JQuery' <https://jquery.com> and 'CSS' styles to allow the display of fireworks on a document. Toolkit to easily incorporate celebratory splashes in 'Rmarkdown' and 'shiny' apps.
	"""
	
	homepage = "https://r2fireworks.obi.obianom.com/"
	cran = "r2fireworks" 

	version("0.1.0", md5="455a2ac8e646a529df20b833dc49fe20")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
