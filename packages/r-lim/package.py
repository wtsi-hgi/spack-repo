# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLim(RPackage):
	"""Linear Inverse Model Examples and Solution Methods

	Functions that read and solve linear inverse problems (food web problems, linear programming problems).
  These problems find solutions to linear or quadratic functions:
  min or max (f(x)), where f(x) = ||Ax-b||^2 or f(x) = sum(ai*xi)
  subject to equality constraints Ex=f and inequality constraints Gx>=h. 
	"""
	
	cran = "LIM" 

	version("1.4.7.1", md5="c3b902baf646b1f0bd96349af544d275")

	depends_on("r@2.1:", type=("build", "run"))
	depends_on("r-limsolve", type=("build", "run"))
	depends_on("r-diagram", type=("build", "run"))
