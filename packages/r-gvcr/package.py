# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGvcr(RPackage):
	"""Genotypic Variance Components

	Functionalities to compute model based genetic components i.e. genotypic variance, phenotypic variance and heritability for given traits of different genotypes from replicated data using methodology explained by Burton, G. W. & Devane, E. H. (1953) (<doi:10.2134/agronj1953.00021962004500100005x>) and Allard, R.W. (2010, ISBN:8126524154).
	"""
	
	homepage = "https://github.com/MYaseen208/gvcR"
	cran = "gvcR" 

	version("0.1.0", md5="9eaf2b9cf4ecf322d8a418fbb95e012e")

	depends_on("r@3.2.3:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-eda4treer", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
