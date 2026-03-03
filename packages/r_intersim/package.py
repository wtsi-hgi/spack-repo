# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIntersim(RPackage):
	"""Simulation of Inter-Related Genomic Datasets

	Generates three inter-related genomic datasets : methylation, gene expression and protein expression.
	"""
	
	cran = "InterSIM" 

	version("2.2.0", md5="2f2c8f936638bbf2502a4db4a1bc1ac6")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-nmf", type=("build", "run"))
