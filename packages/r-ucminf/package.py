# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUcminf(RPackage):
	"""General-Purpose Unconstrained Non-Linear Optimization.

	An algorithm for general-purpose unconstrained non-linear optimization.
	The algorithm is of quasi-Newton type with BFGS updating of the inverse
	Hessian and soft line search with a trust region type monitoring of the
	input to the line search algorithm. The interface of 'ucminf' is designed
	for easy interchange with 'optim'."""

	cran = "ucminf"

	license("GPL-2.0-or-later")

	version("1.2.1", md5="44871c91a7be26117ffad1e685a7b719")

	depends_on("r@3.5:", type=("build", "run"))
