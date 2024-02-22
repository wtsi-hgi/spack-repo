# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSeedcca(RPackage):
	"""Seeded Canonical Correlation Analysis

	Functions for dimension reduction through the seeded canonical correlation analysis are provided. A classical canonical correlation analysis (CCA) is one of useful statistical methods in multivariate data analysis, but it is limited in use due to the matrix inversion for large p small n data. To overcome this, a seeded CCA has been proposed in Im, Gang and Yoo (2015) doi{10.1002/cem.2691}. The seeded CCA is a two-step procedure. The sets of variables are initially reduced by successively projecting cov(X,Y) or cov(Y,X) onto cov(X) and cov(Y), respectively, without loss of information on canonical correlation analysis, following Cook, Li and Chiaromonte (2007) doi{10.1093/biomet/asm038} and Lee and Yoo (2014) doi{10.1111/anzs.12057}. Then, the canonical correlation is finalized with the initially-reduced two sets of variables.
	"""
	
	cran = "seedCCA" 

	version("3.1", md5="db46bb0b315320675a0fe7e3ef347f4c")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-cca", type=("build", "run"))
	depends_on("r-corpcor", type=("build", "run"))
