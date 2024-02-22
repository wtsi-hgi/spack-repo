# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMxsem(RPackage):
	"""Specify 'OpenMx' Models with a 'lavaan'-Style Syntax

	Provides a 'lavaan'-like syntax for 'OpenMx' models. The syntax supports 
  definition variables, bounds, and parameter transformations. This allows for
  latent growth curve models with person-specific measurement occasions, moderated
  nonlinear factor analysis and much more.
	"""
	
	homepage = "https://jhorzek.github.io/mxsem/"
	cran = "mxsem" 

	version("0.0.8", md5="8b1d1fac8695f8897c8e6abe6be3f815")

	depends_on("r-openmx", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
