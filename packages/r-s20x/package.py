# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RS20x(RPackage):
	"""Functions for University of Auckland Course STATS 201/208 Data
Analysis

	A set of functions used in teaching STATS 201/208 Data Analysis at
    the University of Auckland. The functions are designed to make parts of R more
    accessible to a large undergraduate population who are mostly not statistics
    majors.
	"""
	
	homepage = "https://github.com/STATS-UOA/s20x"
	cran = "s20x" 

	version("3.1-40", md5="93dd9c23fe001e5d97ced8fa2ddfea65")

	depends_on("r@4:", type=("build", "run"))
