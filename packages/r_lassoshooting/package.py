# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLassoshooting(RPackage):
	"""L1 Regularized Regression (Lasso) Solver using the Cyclic
Coordinate Descent Algorithm aka Lasso Shooting

	L1 regularized regression (Lasso) solver using the Cyclic
        Coordinate Descent algorithm aka Lasso Shooting is fast. This
        implementation can choose which coefficients to penalize. It
        support coefficient-specific penalties and it can take X'X and
        X'y instead of X and y.
	"""
	
	cran = "lassoshooting" 

	version("0.1.5-1.1", md5="cd0ce678b506de30f248fd945e973890")

	depends_on("r@2.12:", type=("build", "run"))
