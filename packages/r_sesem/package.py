# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSesem(RPackage):
	"""Spatially Explicit Structural Equation Modeling

	Structural equation modeling is a powerful statistical approach for the testing of networks of direct and indirect theoretical causal relationships in complex data sets with inter-correlated dependent and independent variables. Here we implement a simple method for spatially explicit structural equation modeling based on the analysis of variance co-variance matrices calculated across a range of lag distances. This method provides readily interpreted plots of the change in path coefficients across scale.
	"""
	
	homepage = "http://www.r-project.org"
	cran = "sesem" 

	version("1.0.2", md5="f4255d2b3872c92f2f1310ad36f6ce26")

	depends_on("r@1.8:", type=("build", "run"))
	depends_on("r-lavaan", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
