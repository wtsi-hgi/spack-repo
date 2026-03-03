# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHdomdesign(RPackage):
	"""High-Dimensional Orthogonal Maximin Distance Designs

	Contains functions to construct high-dimensional orthogonal maximin distance designs in two, four, eight, and sixteen levels from rotating the Kronecker product of sub-Hadamard matrices. 
	"""
	
	cran = "HDOMDesign" 

	version("1.0-1", md5="b460ca7fac237381ea83e03724e18dd5")

	depends_on("r-hadamardr", type=("build", "run"))
