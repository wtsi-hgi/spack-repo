# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgsci(RPackage):
	"""Scientific Journal and Sci-Fi Themed Color Palettes for 'ggplot2'.

	collection of 'ggplot2' color palettes inspired by plots in scientific
	journals, data visualization libraries, science fiction movies, and TV
	shows."""

	cran = "ggsci"

	license("GPL-3.0-or-later")

	version("3.0.1", md5="364b35c342685528a760417f72399807")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2@2:", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
