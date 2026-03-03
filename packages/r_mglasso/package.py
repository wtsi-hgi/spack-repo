# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMglasso(RPackage):
	"""Multiscale Graphical Lasso

	Inference of Multiscale graphical models with neighborhood
    selection approach.  The method is based on solving a convex
    optimization problem combining a Lasso and fused-group Lasso
    penalties.  This allows to infer simultaneously a conditional
    independence graph and a clustering partition. The optimization is
    based on the Continuation with Nesterov smoothing in a
    Shrinkage-Thresholding Algorithm solver (Hadj-Selem et al. 2018)
    <doi:10.1109/TMI.2018.2829802> implemented in python.
	"""
	
	homepage = "https://desanou.github.io/mglasso/"
	cran = "mglasso" 

	version("0.1.2", md5="fb9fd88cecdae9e08757c9b146b3d802")

	depends_on("r-corpcor", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-r-utils", type=("build", "run"))
	depends_on("r-reticulate@1.25:", type=("build", "run"))
	depends_on("r-rstudioapi", type=("build", "run"))
