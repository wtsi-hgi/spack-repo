# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgpointdensity(RPackage):
	"""A Cross Between a 2D Density Plot and a Scatter Plot

	A cross between a 2D density plot and a scatter plot,
    implemented as a 'ggplot2' geom. Points in the scatter plot are 
    colored by the number of neighboring points. This is useful to
    visualize the 2D-distribution of points in case of overplotting.
	"""
	
	homepage = "https://github.com/LKremer/ggpointdensity"
	cran = "ggpointdensity" 

	version("0.1.0", md5="dbcd919d5bb59f03bb68eed1370aa5c9")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
