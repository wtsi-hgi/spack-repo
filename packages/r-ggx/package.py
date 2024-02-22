# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgx(RPackage):
	"""A Natural Language Interface to 'ggplot2'

	The 'ggplot2' package is the state-of-the-art toolbox for creating and formatting graphs. However, it is easy to forget how certain formatting commands are named and sometimes users find themselves asking: How do you rotate the x-axis labels again? Or how do you hide the legend...? This package allows users to issue natural language commands related to theme-related styling of plots (colors, font size and such), which then are translated into valid 'ggplot2' commands.
	"""
	
	cran = "ggx" 

	version("0.1.1", md5="60fb9ad14c9594ee8898f2ba620dc34f")

	depends_on("r-sets", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
