# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RR2sundials(RPackage):
	"""Wrapper for 'SUNDIALS' Solving ODE and Sensitivity Problem

	Wrapper for widely used 'SUNDIALS' software (SUite of Nonlinear and DIfferential/ALgebraic Equation Solvers) and more precisely to its 'CVODES' solver. It is aiming to solve ordinary differential equations (ODE) and optionally pending forward sensitivity problem. The wrapper is made 'R' friendly by allowing to pass custom parameters to user's callback functions. Such functions can be both written in 'R' and in 'C++' ('RcppArmadillo' flavor). In case of 'C++', performance is greatly improved so this option is highly advisable when performance matters. If provided, Jacobian matrix can be calculated either in dense or sparse format. In the latter case 'rmumps' package is used to solve corresponding linear systems. Root finding and pending event management are optional and can be specified as 'R' or 'C++' functions too. This makes them a very flexible tool for controlling the ODE system during the time course simulation. 'SUNDIALS' library was published in Hindmarsh et al. (2005) <doi:10.1145/1089014.1089020>.
	"""
	
	cran = "r2sundials" 

	version("6.5.0-4", md5="e58e0ecd466c5d9108b2c801ca0b4882")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-rmumps@5.2.1.6:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
