# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDoubt(RPackage):
	"""Enable Operators Containing the '?' Symbol

	Overload utils::'?' to build unary and binary operators from existing functions, 
    piping operators of different precedence, and flexible syntaxes.  
	"""
	
	cran = "doubt" 

	version("0.1.0", md5="44cf71944c15c70c53faca2127480b1b")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-unglue", type=("build", "run"))
