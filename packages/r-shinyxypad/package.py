# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RShinyxypad(RPackage):
	"""XY Controller for 'Shiny'

	Provides an XY pad input for the 'Shiny' framework. An XY pad is like a bivariate slider. It allows to pick up a pair of numbers.
	"""
	
	homepage = "https://github.com/stla/shinyXYpad"
	cran = "shinyXYpad" 

	version("0.2.0", md5="8efe52afadc4e507254e9ceba14c2648")

	depends_on("r-shiny", type=("build", "run"))
