# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAst2ast(RPackage):
	"""Translates an R Function to a C++ Function

	Enable translation of a tiny subset of R to C++. The user has to define a R function which gets translated. For a full list of possible functions check the documentation. After translation an R function is returned which is a shallow wrapper around the C++ code. Alternatively an external pointer to the C++ function is returned to the user. The intention of the package is to generate fast functions which can be used as ode-system or during optimization. 
	"""
	
	homepage = "https://github.com/Konrad1991/ast2ast"
	cran = "ast2ast" 

	version("0.3.2", md5="94a0c5c7fd6dba0ab105c921e99376da")

	depends_on("r-rcpp@1.0.4:", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-dfdr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
