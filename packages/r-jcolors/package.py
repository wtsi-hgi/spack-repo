# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RJcolors(RPackage):
	"""Colors Palettes for R and 'ggplot2', Additional Themes for
'ggplot2'

	Contains a selection of color palettes and 'ggplot2' themes designed by the package author.
	"""
	
	homepage = "https://jaredhuling.org/jcolors/"
	cran = "jcolors" 

	version("0.0.5", md5="429d723324de613372a62522e13b2a3a")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-ggplot2@3:", type=("build", "run"))
