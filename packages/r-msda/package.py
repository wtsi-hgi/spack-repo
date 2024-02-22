# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMsda(RPackage):
	"""Multi-Class Sparse Discriminant Analysis

	Efficient procedures for computing a new Multi-Class Sparse Discriminant Analysis method that estimates all discriminant directions simultaneously. It is an implementation of the work proposed by Mai, Q., Yang, Y., and Zou, H. (2019) <doi:10.5705/ss.202016.0117>. 
	"""
	
	homepage = "https://github.com/emeryyi/msda"
	cran = "msda" 

	version("1.0.3", md5="a4844946b632038ba274c1673f5f9143")

	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
