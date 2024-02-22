# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCode(RPackage):
	"""Automated C Code Generation for 'deSolve', 'bvpSolve'

	Generates all necessary C functions allowing the user to work with
    the compiled-code interface of ode() and bvptwp(). The implementation supports
    "forcings" and "events". Also provides functions to symbolically compute
    Jacobians, sensitivity equations and adjoint sensitivities being the basis for
    sensitivity analysis.
	"""
	
	cran = "cOde" 

	version("1.1.1", md5="0c069113c2944dd9a180a18babf29c2a")

	depends_on("r@3:", type=("build", "run"))
