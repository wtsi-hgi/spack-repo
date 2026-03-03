# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBayesx(RPackage):
	"""R Utilities Accompanying the Software Package BayesX

	Functions for exploring and visualising estimation results
  obtained with BayesX, a free software for estimating structured additive
  regression models (<https://www.uni-goettingen.de/de/bayesx/550513.html>). In addition,
  functions that allow to read, write and manipulate map objects that are required in spatial
  analyses performed with BayesX.
	"""
	
	cran = "BayesX" 

	version("0.3-3", md5="cfbb93a442986179c2d938c298d15052")

	depends_on("r-shapefiles", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-colorspace", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-interp", type=("build", "run"))
