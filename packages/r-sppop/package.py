# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSppop(RPackage):
	"""Generation of Spatial Population under Different Levels of
Relationships among Variables

	The developed package can be used to generate a spatial population for different
             levels of relationships among the dependent and auxiliary variables along with spatially
             varying model parameters. A spatial layout is designed as a [0,k-1]x[0,k-1] square region on which observations
             are collected at (k x k) lattice points with a unit distance between any two neighbouring points along the horizontal
             and vertical axes. For method details see Chao, Liu., Chuanhua, Wei. and Yunan, Su. (2018).<doi:10.1080/10485252.2018.1499907>.
             The generated spatial population can be utilized in Geographically Weighted Regression model based analysis for studying the 
             spatially varying relationships among the variables. Furthermore, various statistical analysis can be performed on this spatially 
             generated data.
	"""
	
	cran = "SpPOP" 

	version("0.1.0", md5="40b15b61c2cc2fac8154b950d4e3cf7f")

	depends_on("r-qpdf", type=("build", "run"))
	depends_on("r-numbers", type=("build", "run"))
