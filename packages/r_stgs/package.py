# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStgs(RPackage):
	"""Genomic Selection using Single Trait

	Genomic Selection (GS) is a latest development in animal and plant breeding where whole genome markers information is used to predict genetic merit of an individuals in a practical breeding programme. GS is one of the promising tool for improving genetic gain in animal and plants in today’s scenario. This package is basically developed for genomic predictions by estimating marker effects. These marker effects further used for calculation of genotypic merit of individual i.e. genome estimated breeding values (GEBVs). Genomic selection may be based on single trait or multi traits information. This package performs genomic selection only for single traits hence named as STGS i.e. single trait genomic selection. STGS is a comprehensive package which gives single step solution for genomic selection based on most commonly used statistical methods. 
	"""
	
	cran = "STGS" 

	version("0.1.0", md5="be4e2f9db0164b5b7ea2ed24440b71c6")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-brnn", type=("build", "run"))
	depends_on("r-kernlab", type=("build", "run"))
	depends_on("r-randomforest", type=("build", "run"))
	depends_on("r-rrblup", type=("build", "run"))
