# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQuollr(RPackage):
	"""Visualising How Nonlinear Dimension Reduction Warps Your Data

	To construct a model in 2D
    space from 2D embedding data and then lift it to the high-dimensional
    space. Additionally, it provides tools to visualize the model in 2D
    space and to overlay the fitted model on data using the tour
    technique. Furthermore, it facilitates the generation of summaries of
    high-dimensional distributions.
	"""
	
	homepage = "https://github.com/JayaniLakshika/quollr"
	cran = "quollr" 

	version("0.1.1", md5="ea40b2fbdecaefbaea1c1411a6963b01")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-interp@1.1.6:", type=("build", "run"))
	depends_on("r-langevitour", type=("build", "run"))
	depends_on("r-proxy", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rsample", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
