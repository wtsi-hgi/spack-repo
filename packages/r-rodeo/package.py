# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRodeo(RPackage):
	"""A Code Generator for ODE-Based Models

	Provides an R6 class and several utility methods to
    facilitate the implementation of models based on ordinary
    differential equations. The heart of the package is a code generator
    that creates compiled 'Fortran' (or 'R') code which can be passed to
    a numerical solver. There is direct support for solvers contained
    in packages 'deSolve' and 'rootSolve'.
	"""
	
	homepage = "https://github.com/dkneis/rodeo"
	cran = "rodeo" 

	version("0.7.8", md5="f7fabbab0b7d86e96e82dad661c114b6")

	depends_on("r-r6", type=("build", "run"))
	depends_on("r-desolve", type=("build", "run"))
	depends_on("gcc", type=("build", "link", "run"))
