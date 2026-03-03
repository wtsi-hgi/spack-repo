# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDynrb(RPackage):
	"""Dynamic Range Boxes

	Improves the concept of multivariate range boxes, which is highly susceptible for outliers and does not consider the distribution of the data. The package uses dynamic range boxes to overcome these problems.
	"""
	
	cran = "dynRB" 

	version("0.18", md5="ec816b51605866194d36c07d9c53e04c")

	depends_on("r-corrplot", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-vegan", type=("build", "run"))
	depends_on("r-foreign", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
