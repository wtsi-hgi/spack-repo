# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDisimformixed(RPackage):
	"""Calculate Dissimilarity Matrix for Dataset with Mixed Attributes

	Implement the methods proposed by Ahmad & Dey (2007) <doi:10.1016/j.datak.2007.03.016> in calculating the dissimilarity matrix at the presence of mixed attributes. This Package includes functions to discretize quantitative variables, calculate conditional probability for each pair of attribute values, distance between every pair of attribute values, significance of attributes, calculate dissimilarity between each pair of objects.
	"""
	
	cran = "DisimForMixed" 

	version("0.2", md5="f0261e548e15c1a104e43a8f61b0b9f4")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
