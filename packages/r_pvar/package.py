# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPvar(RPackage):
	"""Calculation and Application of p-Variation

	The calculation of p-variation of the finite sample data. 
	This package is a realisation of the procedure described in Butkus, V. & Norvaisa, R. Lith Math J (2018). <doi: 10.1007/s10986-018-9414-3>
	The formal definitions and reference into literature are given in vignette.
	"""
	
	cran = "pvar" 

	version("2.2.7", md5="34bd99e6d5d09b97966e4a8128c6111d")

	depends_on("r-rcpp", type=("build", "run"))
