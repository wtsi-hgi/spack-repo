# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RColors3d(RPackage):
	"""Generate 2D and 3D Color Palettes

	Generate multivariate color palettes to represent two-dimensional or three-dimensional data in graphics (in contrast to standard color palettes that represent just one variable). You tell 'colors3d' how to map color space onto your data, and it gives you a color for each data point. You can then use these colors to make plots in base 'R', 'ggplot2', or other graphics frameworks.
	"""
	
	homepage = "https://github.com/matthewkling/colors3d"
	cran = "colors3d" 

	version("1.0.1", md5="71e0fdfca1cb99b4bcbb23a347239164")

	depends_on("r@3.2.2:", type=("build", "run"))
	depends_on("r-combinat", type=("build", "run"))
	depends_on("r-fnn", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
