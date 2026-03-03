# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCols(RPackage):
	"""Constrained Ordinary Least Squares

	Constrained ordinary least squares is performed. One constraint is that all beta coefficients (including the constant) cannot be negative. They can be either 0 or strictly positive. Another constraint is that the sum of the beta coefficients equals a constant. References: Hansen, B. E. (2022). Econometrics, Princeton University Press. <ISBN:9780691235899>.
	"""
	
	cran = "cols" 

	version("1.1", md5="94792ef3ecaa4aed4372031c2eee9e68")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-quadprog", type=("build", "run"))
	depends_on("r-rfast2", type=("build", "run"))
