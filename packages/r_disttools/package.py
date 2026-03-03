# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDisttools(RPackage):
	"""Distance Object Manipulation Tools

	Provides convenient methods for accessing the data in 'dist' objects with minimal memory and computational overhead. 'disttools' can be used to extract the distance between any pair or combination of points encoded by a 'dist' object using only the indices of those points. This is an improvement over existing functionality, which requires either coercing a 'dist' object into a matrix or calculating the one dimensional index corresponding to a pair of observations. Coercion to a matrix is undesirable because doing so doubles the amount of memory required for storage. In contrast, there is no inherent downside to the latter solution. However, in part due to several edge cases, correctly and efficiently implementing such a solution can be challenging. 'disttools' abstracts away these challenges and provides a simple interface to access the data in a 'dist' object using the latter approach.
	"""
	
	cran = "disttools" 

	version("0.1.8", md5="fa02762c12f603ed02ab498ddb838d9d")

