# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAsymmetry(RPackage):
	"""Multidimensional Scaling of Asymmetric Proximities

	Multidimensional scaling models and methods for the visualization and analysis of asymmetric proximity data <doi:10.1111/j.2044-8317.1996.tb01078.x>. An asymmetric data matrix has the same number of rows and columns, and these rows and columns refer to the same set of objects. At least some elements in the upper-triangle are different from the corresponding elements in the lower triangle. An example of an asymmetric matrix is a  student migration table, where the rows correspond to the countries of origin of the students and the columns to the destination countries. This package provides algorithms for three multidimensional scaling models. These are the slide-vector model <doi:10.1007/BF02294474>, a scaling model with unique dimensions and the asymscal model for asymmetric multidimensional scaling. Furthermore, a heat map for skew-symmetric data, and the decomposition of asymmetry are provided for the exploratory analysis of asymmetric tables.
	"""
	
	cran = "asymmetry" 

	version("2.0.4", md5="515e941004e48b865983c3d6717230b3")

	depends_on("r-gplots", type=("build", "run"))
	depends_on("r-smacof", type=("build", "run"))
