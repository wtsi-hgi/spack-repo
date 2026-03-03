# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLdrtools(RPackage):
	"""Tools for Linear Dimension Reduction

	Linear dimension reduction subspaces can be uniquely defined using orthogonal projection matrices. This package provides tools to compute distances between such subspaces and to compute the average subspace. For details see Liski, E.Nordhausen K., Oja H., Ruiz-Gazen A. (2016) Combining Linear Dimension Reduction Subspaces <doi:10.1007/978-81-322-3643-6_7>.
	"""
	
	cran = "LDRTools" 

	version("0.2-2", md5="259abc3abab002409fa65f6057f9c747")

	depends_on("r@3.2.2:", type=("build", "run"))
