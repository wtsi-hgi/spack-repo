# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStpp(RPackage):
	"""Space-Time Point Pattern Simulation, Visualisation and Analysis

	Many of the models encountered in applications of point process methods to the study of spatio-temporal phenomena are covered in 'stpp'. This package provides statistical tools for analyzing the global and local second-order properties of spatio-temporal point processes, including estimators of the space-time inhomogeneous K-function and pair correlation function. It also includes tools to get static and dynamic display of spatio-temporal point patterns. See Gabriel et al (2013) <doi:10.18637/jss.v053.i02>.
	"""
	
	cran = "stpp" 

	version("2.0-7", md5="2902365dcf5585cf3fbb47633a127421")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-rpanel", type=("build", "run"))
	depends_on("r-splancs", type=("build", "run"))
	depends_on("r-kernsmooth", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-plot3d", type=("build", "run"))
	depends_on("r-rgl", type=("build", "run"))
	depends_on("r-spatstat-explore", type=("build", "run"))
	depends_on("r-spatstat-geom", type=("build", "run"))
	depends_on("r-spatstat-random", type=("build", "run"))
