# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTurtlegraphics(RPackage):
	"""Turtle Graphics

	An implementation of turtle graphics
    <http://en.wikipedia.org/wiki/Turtle_graphics>.
    Turtle graphics comes from Papert's language Logo and has
    been used to teach concepts of computer programming.
	"""
	
	homepage = "http://www.gagolewski.com/software/TurtleGraphics/"
	cran = "TurtleGraphics" 

	version("1.0-8", md5="6a0953e3deee9ab1ffea4c11c1f62e3b")

	depends_on("r@3:", type=("build", "run"))
