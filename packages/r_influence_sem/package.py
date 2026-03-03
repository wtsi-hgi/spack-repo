# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RInfluenceSem(RPackage):
	"""Case Influence in Structural Equation Models

	A set of tools for evaluating several measures of case influence for structural equation models. 
	"""
	
	cran = "influence.SEM" 

	version("2.3", md5="f2d1cf71e344e257a09765eeff1cb9d7")

	depends_on("r-lavaan", type=("build", "run"))
