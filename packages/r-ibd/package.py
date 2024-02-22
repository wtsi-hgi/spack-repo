# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIbd(RPackage):
	"""Incomplete Block Designs

	A collection of several utility functions related to binary incomplete block designs. Contains function to generate A- and D-efficient binary incomplete block designs with given numbers of treatments, number of blocks and block size. Contains function to generate an incomplete block design with specified concurrence matrix. There are functions to generate balanced treatment incomplete block designs and incomplete block designs for test versus control treatments comparisons with specified concurrence matrix. Allows performing analysis of variance of data and computing estimated marginal means of factors from experiments using a connected incomplete block design. Tests of hypothesis of treatment contrasts in incomplete block design set up is supported. 
	"""
	
	cran = "ibd" 

	version("1.6", md5="79f4fc14b616624fb1f65254e0a03b83")

	depends_on("r@3.1.1:", type=("build", "run"))
	depends_on("r-lpsolve", type=("build", "run"))
	depends_on("r-car", type=("build", "run"))
	depends_on("r-emmeans", type=("build", "run"))
	depends_on("r-multcomp", type=("build", "run"))
