# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RThematic(RPackage):
	"""Unified and Automatic 'Theming' of 'ggplot2', 'lattice', and
'base' R Graphics

	Theme 'ggplot2', 'lattice', and 'base' graphics based on a
    few choices, including foreground color, background color, accent
    color, and font family. Fonts that aren't available on the system, but
    are available via download on 'Google Fonts', can be automatically
    downloaded, cached, and registered for use with the 'showtext' and
    'ragg' packages.
	"""
	
	homepage = "https://rstudio.github.io/thematic/"
	cran = "thematic" 

	version("0.1.5", md5="bc28cf1befc33f91bfc9b647b1b01adb")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-farver", type=("build", "run"))
	depends_on("r-ggplot2@3.3:", type=("build", "run"))
	depends_on("r-rappdirs", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rstudioapi@0.8:", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
