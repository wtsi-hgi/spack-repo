# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RInterep(RPackage):
	"""Interaction Analysis of Repeated Measure Data

	Extensive penalized variable selection methods have been developed in the past two decades for analyzing high dimensional omics data, such as gene expressions, single nucleotide polymorphisms (SNPs), copy number variations (CNVs) and others. However, lipidomics data have been rarely investigated by using high dimensional variable selection methods. This package incorporates our recently developed penalization procedures to conduct interaction analysis for high dimensional lipidomics data with repeated measurements. The core module of this package is developed in C++. The development of this software package and the associated statistical methods have been partially supported by an Innovative Research Award from Johnson Cancer Research Center, Kansas State University.
	"""
	
	homepage = "https://github.com/feizhoustat/interep"
	cran = "interep" 

	version("0.4.1", md5="308bab2d97bf46abf82bff9880a8735e")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
