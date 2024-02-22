# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPeacockTest(RPackage):
	"""Two and Three Dimensional Kolmogorov-Smirnov Two-Sample Tests

	The original definition of the two and three dimensional Kolmogorov-Smirnov two-sample
             test statistics given by Peacock (1983) is implemented. Two R-functions: peacock2 and peacock3, 
             are provided to compute the test statistics in two and three dimensional spaces, respectively. 
             Note the Peacock test is different from the Fasano and Franceschini test (1987). The latter is 
             a variant of the Peacock test.
	"""
	
	cran = "Peacock.test" 

	version("1.0", md5="18a5351a54dbbe23e0839bc26397d449")

