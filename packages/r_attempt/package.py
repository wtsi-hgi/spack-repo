# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAttempt(RPackage):
	"""Tools for Defensive Programming

	Tools for defensive programming, inspired by 'purrr' mappers and 
    based on 'rlang'.'attempt' extends and facilitates defensive programming by 
    providing a consistent grammar, and provides a set of easy to use functions 
    for common tests and conditions. 'attempt' only depends on 'rlang', and 
    focuses on speed, so it can be easily integrated in other functions and 
    used in data analysis. 
	"""
	
	homepage = "https://github.com/ColinFay/attempt"
	cran = "attempt" 

	version("0.3.1", md5="b4cbba3e4a87008b3aa8c60251576ccc")

	depends_on("r-rlang", type=("build", "run"))
