# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMultinttestfunc(RPackage):
	"""Provides Test Functions for Multivariate Integration

	Provides implementations of functions that can be used to
    test multivariate integration routines. The package covers six
    different integration domains (unit hypercube, unit ball, unit sphere,
    standard simplex, non-negative real numbers and R^n). For each domain
    several functions with different properties (smooth,
    non-differentiable, ...) are available. The functions are available in
    all dimensions n >= 1. For each function the exact value of the
    integral is known and implemented to allow testing the accuracy of
    multivariate integration routines. Details on the available test
    functions can be found at on the development website.
	"""
	
	homepage = "https://github.com/KlausHerrmann/multIntTestFunc"
	cran = "multIntTestFunc" 

	version("0.2.0", md5="be7f0bf760ebe4f0254aa857b255d715")

	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
