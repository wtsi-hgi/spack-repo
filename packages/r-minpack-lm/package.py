# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMinpackLm(RPackage):
	"""R Interface to the Levenberg-Marquardt Nonlinear Least-Squares
Algorithm Found in MINPACK, Plus Support for Bounds

	The nls.lm function provides an R interface to lmder and lmdif from the MINPACK library, for solving nonlinear least-squares problems by a modification of the Levenberg-Marquardt algorithm, with support for lower and upper parameter bounds.  The implementation can be used via nls-like calls using the nlsLM function.  
	"""
	
	cran = "minpack.lm" 

	version("1.2-4", md5="f1cda9e2b12e4a6e3ea63c165642797e")

