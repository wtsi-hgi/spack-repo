# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDesolve(RPackage):
	"""Solvers for Initial Value Problems of Differential Equations ('ODE',
	'DAE', 'DDE').

	Functions that solve initial value problems of a system of first-order
	ordinary differential equations ('ODE'), of partial differential equations
	('PDE'), of differential algebraic equations ('DAE'), and of delay
	differential equations.  The functions provide an interface to the FORTRAN
	functions 'lsoda', 'lsodar', 'lsode', 'lsodes' of the 'ODEPACK' collection,
	to the FORTRAN functions 'dvode', 'zvode' and 'daspk' and a
	C-implementation of solvers of the 'Runge-Kutta' family with fixed or
	variable time steps.  The package contains routines designed for solving
	'ODEs' resulting from 1-D, 2-D and 3-D partial differential equations
	('PDE') that have been converted to 'ODEs' by numerical differencing."""

	cran = "deSolve"

	version("1.40", md5="50361fb9eef3e96c00387476509dfe5d")

	depends_on("r@3.3:", type=("build", "run"))
