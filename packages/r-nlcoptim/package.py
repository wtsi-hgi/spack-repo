# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNlcoptim(RPackage):
	"""Solve Nonlinear Optimization with Nonlinear Constraints

	Optimization for nonlinear objective and constraint functions.  Linear or nonlinear equality and inequality constraints are allowed.  It accepts the input parameters as a constrained matrix.
	"""
	
	cran = "NlcOptim" 

	version("0.6", md5="33edd0e3fa53afc70d81a166351d989b")

	depends_on("r-mass", type=("build", "run"))
	depends_on("r@3.2.2:", type=("build", "run"))
	depends_on("r-quadprog", type=("build", "run"))
