# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTropalgebra(RPackage):
	"""Tropical Algebraic Functions

	It includes functions like tropical addition, tropical multiplication for vectors and matrices. In tropical algebra, the tropical sum of two numbers is their minimum and the tropical product of two numbers is their ordinary sum. For more information see also I. Simon (1988) Recognizable sets with multiplicities in the tropical semi ring: Volume 324 Lecture Notes I Computer Science, pages 107-120 <doi: 10.1007/BFb0017135>.
	"""
	
	cran = "tropAlgebra" 

	version("0.1.1", md5="62dd3acceec9c9da513b631ec15f1fdc")

	depends_on("r@3.3:", type=("build", "run"))
