# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTvthemes(RPackage):
	"""TV Show Themes and Color Palettes for 'ggplot2' Graphics

	Contains various 'ggplot2' themes and color palettes based on TV shows 
    such as 'Game of Thrones', 'Brooklyn Nine-Nine', 'Avatar: The Last Airbender',
    'Spongebob Squarepants', and more.
	"""
	
	homepage = "https://github.com/Ryo-N7/tvthemes"
	cran = "tvthemes" 

	version("1.3.3", md5="7e00134655c8fe8fb3cfdde0673d56dc")
	version("1.3.2", md5="d1820c2fb8a697eb1b6d06f403592c1a")

	depends_on("r-ggplot2@3.1:", type=("build", "run"))
	depends_on("r-extrafont@0.17:", type=("build", "run"))
	depends_on("r-scales@1:", type=("build", "run"))
	depends_on("r-magick@2:", type=("build", "run"))
