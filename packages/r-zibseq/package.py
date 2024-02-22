# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RZibseq(RPackage):
	"""Differential Abundance Analysis for Metagenomic Data via
Zero-Inflated Beta Regression

	Detects abundance differences across clinical conditions. Besides, it takes the sparse nature of metagenomic data into account and handles compositional data efficiently.
	"""
	
	cran = "ZIBseq" 

	version("1.2", md5="75bc57898daaeab5e2a88fbc8c121394")

	depends_on("r@3.3.1:", type=("build", "run"))
	depends_on("r-gamlss", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-gamlss-dist", type=("build", "run"))
