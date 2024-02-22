# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RShock(RPackage):
	"""Slope Heuristic for Block-Diagonal Covariance Selection in High
Dimensional Gaussian Graphical Models

	Block-diagonal covariance selection for high dimensional Gaussian
    graphical models. The selection procedure is based on the slope heuristics.
	"""
	
	cran = "shock" 

	version("1.0", md5="3e11648115ed1125fb0b89ed96c7ab24")

	depends_on("r-glasso", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-capushe", type=("build", "run"))
	depends_on("r-ggmselect", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
