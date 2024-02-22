# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBoptbd(RPackage):
	"""Bayesian Optimal Block Designs

	Computes Bayesian A- and D-optimal block designs under the linear mixed effects model settings 
	using block/array exchange algorithm of Debusho, Gemechu and Haines (2018) <doi:10.1080/03610918.2018.1429617> where the interest is in a 
	comparison of all possible elementary treatment contrasts. The package also provides an optional 
	method of using the graphical user interface (GUI) R package 'tcltk' to ensure that it is user friendly.
	"""
	
	cran = "Boptbd" 

	version("1.0.5", md5="b141aa9696b615b7a0ec259a028ae45c")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
