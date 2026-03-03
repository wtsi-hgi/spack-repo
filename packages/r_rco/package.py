# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRco(RPackage):
	"""The R Code Optimizer

	Automatically apply different strategies to optimize R code. 
    'rco' functions take R code as input, and returns R code as output.
	"""
	
	homepage = "https://jcrodriguez1989.github.io/rco/"
	cran = "rco" 

	version("1.0.2", md5="7c8a3e6d4cb8ffe32cdba33103fe25ad")

	depends_on("r@3.6:", type=("build", "run"))
