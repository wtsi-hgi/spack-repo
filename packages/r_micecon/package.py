# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMicecon(RPackage):
	"""Microeconomic Analysis and Modelling

	Various tools for microeconomic analysis and microeconomic modelling,
   e.g. estimating quadratic, Cobb-Douglas and Translog functions,
   calculating partial derivatives and elasticities of these functions,
   and calculating Hessian matrices, checking curvature
   and preparing restrictions for imposing monotonicity of Translog functions.
	"""
	
	homepage = "http://www.micEcon.org"
	cran = "micEcon" 

	version("0.6-18", md5="1f96852792cf02a460f74c1876bfe7e5")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-misctools@0.6.1:", type=("build", "run"))
	depends_on("r-plm@1.1.0:", type=("build", "run"))
