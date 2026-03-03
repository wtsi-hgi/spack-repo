# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCheckarg(RPackage):
	"""Check the Basic Validity of a (Function) Argument

	Utility functions that allow checking the basic validity of a function argument or any other value, 
             including generating an error and assigning a default in a single line of code. The main purpose of
             the package is to provide simple and easily readable argument checking to improve code robustness. 
	"""
	
	cran = "checkarg" 

	version("0.1.0", md5="339debf43f17bd46428ee39d72875a9e")

	depends_on("r@3.1:", type=("build", "run"))
