# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLongrpart2(RPackage):
	"""Recursive Partitioning of Longitudinal Data

	Performs recursive partitioning of linear and nonlinear mixed effects models,
    specifically for longitudinal data. The package is an
    extension of the original 'longRPart' package by 
    Stewart and Abdolell (2013) <https://cran.r-project.org/package=longRPart>. 
	"""
	
	cran = "longRPart2" 

	version("0.2.3", md5="cf8e4f61e9af8014ad74d7970aa11c3a", url="https://cran.r-project.org/src/contrib/longRPart2_0.2.3.tar.gz")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rpart", type=("build", "run"))
	depends_on("r-formula-tools", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
