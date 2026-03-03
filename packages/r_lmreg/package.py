# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLmreg(RPackage):
	"""Data and Functions Used in Linear Models and Regression with R:
An Integrated Approach

	Data files and a few functions used in the book 
             'Linear Models and Regression with R: An Integrated Approach' 
             by Debasis Sengupta and Sreenivas Rao Jammalamadaka (2019).
	"""
	
	cran = "lmreg" 

	version("1.2", md5="611b33a014c2b571e25bdae29a726fb2")

	depends_on("r-mass", type=("build", "run"))
