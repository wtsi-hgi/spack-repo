# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RImp(RPackage):
	"""Interactive Model Performance Evaluation

	Contains functions for evaluating & comparing the performance of Binary classification models. Functions can be called either statically or interactively (as Shiny Apps).
	"""
	
	homepage = "https://github.com/anup50695/IMPPackage"
	cran = "IMP" 

	version("1.1", md5="229905fd604e21b1a12cc40c24951e42")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
