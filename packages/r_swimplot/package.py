# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSwimplot(RPackage):
	"""Tools for Creating Swimmers Plots using 'ggplot2'

	Used for creating swimmers plots with functions to customize the bars, add points, add lines, add text, and add arrows.
	"""
	
	cran = "swimplot" 

	version("1.2.0", md5="fd445cebe101235965c92ab68545a469")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
