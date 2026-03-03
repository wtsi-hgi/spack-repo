# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRmerec(RPackage):
	"""MEREC - Method Based on the Removal Effects of Criteria

	Implementation of the MEthod based on the Removal Effects of Criteria - MEREC- a new objective weighting method for determining criteria weights for Multiple Criteria Decision Making problems, created by Mehdi Keshavarz-Ghorabaee (2021) <doi:10.3390/sym13040525>. Given a decision matrix, the function return the Merec´s weight vector and all intermediate matrix/vectors used to calculate it.
	"""
	
	homepage = "https://github.com/lucassp/rmerec"
	cran = "rmerec" 

	version("0.1.1", md5="85146d9fd59edee7b9582dd95884d092")

