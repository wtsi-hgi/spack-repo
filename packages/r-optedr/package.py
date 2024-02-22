# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROptedr(RPackage):
	"""Calculating Optimal and D-Augmented Designs

	Calculates D-, Ds-, A- and I-optimal designs for non-linear models, via an implementation of the cocktail algorithm (Yu, 2011, <doi:10.1007/s11222-010-9183-2>). Compares designs via their efficiency, and D-augments any design with a controlled efficiency. An efficient rounding function has been provided to transform approximate designs to exact designs.
	"""
	
	homepage = "https://github.com/kezrael/optedr"
	cran = "optedr" 

	version("2.0.0", md5="9d0c79f20fb8e3d8cf1fbb1ec892ea44")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-nleqslv", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
