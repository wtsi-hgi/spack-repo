# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSde(RPackage):
	"""Simulation and Inference for Stochastic Differential Equations

	Companion package to the book Simulation and Inference for
        Stochastic Differential Equations With R Examples, ISBN
        978-0-387-75838-1, Springer, NY.
	"""
	
	cran = "sde" 

	version("2.0.18", md5="9191ac9c3f9c7075942c59d27dd70240")

	depends_on("r-mass", type=("build", "run"))
	depends_on("r-fda", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
