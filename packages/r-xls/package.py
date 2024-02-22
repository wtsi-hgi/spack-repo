# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RXls(RPackage):
	"""A Modeling Approach that Optimizes Future Errors in Least
Squares

	Given the date column as an ascending entry, future errors are included in the sum of squares of error that should be minimized based on the number of steps and weights you determine. Thus, it is prevented that the variables affect each other's coefficients unrealistically.
	"""
	
	cran = "XLS" 

	version("0.1.0", md5="1ee7be7f8d202d356bffbc54ee4a900b")

	depends_on("r-mpoly", type=("build", "run"))
