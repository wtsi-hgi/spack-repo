# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNlmeu(RPackage):
	"""Datasets and Utility Functions Enhancing Functionality of 'nlme'
Package

	Datasets and utility  functions enhancing functionality of nlme package. Datasets, functions and scripts are described in book titled 'Linear Mixed-Effects Models:
 A Step-by-Step Approach' by Galecki and Burzykowski (2013). Package is under development.
	"""
	
	homepage = "http://www-personal.umich.edu/~agalecki/"
	cran = "nlmeU" 

	version("0.70-9", md5="0fa74cfe5817650f768fd5f27ef21d58")

	depends_on("r@2.14.2:", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
