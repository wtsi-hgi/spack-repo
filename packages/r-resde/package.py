# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RResde(RPackage):
	"""Estimation in Reducible Stochastic Differential Equations

	Maximum likelihood estimation for univariate reducible
 stochastic differential equation models. Discrete, possibly noisy
 observations, not necessarily evenly spaced in time. Can fit
 multiple individuals/units with global and local parameters, by
 fixed-effects or mixed-effects methods. Ref.: Garcia, O. (2019)
 "Estimating reducible stochastic differential equations by
 conversion to a least-squares problem", Computational Statistics
 34(1): 23-46, <doi:10.1007/s00180-018-0837-4>.
	"""
	
	homepage = "https://github.com/ogarciav/resde/"
	cran = "resde" 

	version("1.1", md5="44eb1b5547b174fed5cc27adb81a076c")

	depends_on("r-deriv", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
