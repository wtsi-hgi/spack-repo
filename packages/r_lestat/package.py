# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLestat(RPackage):
	"""A Package for Learning Statistics

	Some simple objects and functions to do 
             statistics using linear models and a Bayesian framework. 
	"""
	
	cran = "lestat" 

	version("1.9", md5="5781b4b44f1625f25861cd8984af1548")

	depends_on("r@1.8:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
