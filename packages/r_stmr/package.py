# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStmr(RPackage):
	"""Strength Training Manual R-Language Functions

	Strength training prescription using percent-based approach requires
    numerous computations and assumptions. 'STMr' package allow users to estimate 
    individual reps-max relationships, implement various progression tables, and
    create numerous set and rep schemes. The 'STMr' package is originally created as
    a tool to help writing Jovanović M. (2020) Strength Training Manual
    <ISBN:979-8604459898>.
	"""
	
	homepage = "https://mladenjovanovic.github.io/STMr/"
	cran = "STMr" 

	version("0.1.6", md5="64b5671549dc8e4de4cfb4af80afcf05")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggfittext", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-minpack-lm", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-quantreg", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
