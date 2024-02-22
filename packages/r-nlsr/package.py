# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNlsr(RPackage):
	"""Functions for Nonlinear Least Squares Solutions - Updated 2022

	Provides tools for working with nonlinear least squares problems.
      For the estimation of models reliable and robust tools than nls(), where the
      the Gauss-Newton method frequently stops with 'singular gradient' messages. 
      This is accomplished by using, where possible, analytic derivatives to compute
      the matrix of derivatives and a stabilization of the solution of the estimation
      equations. Tools for approximate or externally supplied derivative matrices
      are included. Bounds and masks on parameters are handled properly.
	"""
	
	cran = "nlsr" 

	version("2023.8.31", md5="b461e18912259e51fd07889e246e3843")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
