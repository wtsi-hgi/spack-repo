# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRrapply(RPackage):
	"""Revisiting Base Rapply

	The minimal 'rrapply'-package contains a single function rrapply(), providing an extended implementation of 'R'-base rapply() by allowing to recursively apply a function to elements of a nested list based on a general condition function and including the possibility to prune or aggregate nested list elements from the result. In addition, special arguments can be supplied to access the name, location, parents and siblings in the nested list of the element under evaluation. The rrapply() function builds upon rapply()'s native 'C' implementation and requires no other package dependencies.
	"""
	
	homepage = "https://jorischau.github.io/rrapply/"
	cran = "rrapply" 

	version("1.2.6", md5="62e94e2c8400acfe6a5611e43d06d6c6")

	depends_on("r@3.5:", type=("build", "run"))
