# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLindenmayer(RPackage):
	"""Functions to Explore L-Systems (Lindenmayer Systems)

	L-systems or Lindenmayer systems are parallel rewriting systems which can
    be used to simulate biological forms and certain kinds of fractals.
    Briefly, in an L-system a series of symbols in a string are replaced
    iteratively according to rules to give a more complex string. Eventually,
    the symbols are translated into turtle graphics for plotting. Wikipedia has
    a very good introduction: en.wikipedia.org/wiki/L-system This package
    provides basic functions for exploring L-systems.
	"""
	
	cran = "LindenmayeR" 

	version("0.1.13", md5="2bb682a42d4c5be1d1ecf7ad92241c94")

	depends_on("r-stringr", type=("build", "run"))
