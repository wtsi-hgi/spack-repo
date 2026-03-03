# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSeedreg(RPackage):
	"""Regression Analysis for Seed Germination as a Function of
Temperature

	Regression analysis using common models in seed temperature studies, such as the Gaussian model (Martins, JF, Barroso, AAM, & Alves, PLCA (2017) <doi:10.1590/s0100-83582017350100039>), quadratic (Nunes, AL, Sossmeier, S, Gotz, AP, & Bispo, NB (2018) <doi: 10.17265/2161-6264/2018.06.002>) and others with potential for use, such as those implemented in the 'drc' package (Ritz, C, Baty, F, Streibig, JC, & Gerhard, D (2015). <doi:10.1371/journal.pone.0146021>), in the estimation of the ideal and cardinal temperature for the occurrence of plant seed germination. The functions return graphs with the equations automatically.
	"""
	
	cran = "seedreg" 

	version("1.0.3", md5="bb7a92f7bcdac7c07c358828f592c986")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-drc", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-car", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-emmeans", type=("build", "run"))
	depends_on("r-multcomp", type=("build", "run"))
	depends_on("r-hnp", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-multcompview", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
