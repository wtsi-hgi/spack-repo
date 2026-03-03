# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRootsolve(RPackage):
	"""Nonlinear Root Finding, Equilibrium and Steady-State Analysis of
Ordinary Differential Equations

	Routines to find the root of nonlinear functions, and to perform steady-state and equilibrium analysis of ordinary differential equations (ODE). 
  Includes routines that: (1) generate gradient and jacobian matrices (full and banded),
  (2) find roots of non-linear equations by the 'Newton-Raphson' method, 
  (3) estimate steady-state conditions of a system of (differential) equations in full, banded or sparse form, using the 'Newton-Raphson' method, or by dynamically running,
  (4) solve the steady-state conditions for uni-and multicomponent 1-D, 2-D, and 3-D partial differential equations, that have been converted to ordinary differential equations
    by numerical differencing (using the method-of-lines approach).
  Includes fortran code.
	"""
	
	cran = "rootSolve" 

	version("1.8.2.4", md5="55edadf34bf9065e60c7570e82bc4b16")

	depends_on("r@2.1:", type=("build", "run"))
