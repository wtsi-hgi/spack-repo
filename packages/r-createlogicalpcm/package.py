# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCreatelogicalpcm(RPackage):
	"""Create Logical Pairwise Comparison Matrix for the Analytic
Hierarchy Process

	Create Pairwise Comparison Matrices for use in the Analytic Hierarchy Process. The Pairwise Comparison Matrix created will be a logical matrix, which unlike a random comparison matrix, is similar to what a rational decision maker would create on the basis of a preference vector for the alternatives considered.
	"""
	
	cran = "createLogicalPCM" 

	version("0.1.0", md5="628516d2533c36a45309895eba32ce9f")

