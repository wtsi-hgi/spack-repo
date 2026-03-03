# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPagwas(RPackage):
	"""Pathway Analysis Methods for Genomewide Association Data

	Bayesian hierarchical methods for pathway analysis of genomewide association data: Normal/Bayes factors and Sparse Normal/Adaptive lasso. The Frequentist Fisher's product method is included as well.
	"""
	
	cran = "PAGWAS" 

	version("2.0", md5="041f4dd97db063c91f27b50d447ea150")

	depends_on("r-lars", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-mnormt", type=("build", "run"))
