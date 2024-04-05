# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSymengine(RPackage):
	"""Interface to the 'SymEngine' Library

	
    Provides an R interface to 'SymEngine' <https://github.com/symengine/>,
    a standalone 'C++' library for fast symbolic manipulation. The package has functionalities
    for symbolic computation like calculating exact mathematical expressions, solving
    systems of linear equations and code generation.
	"""
	
	homepage = "https://github.com/symengine/symengine.R"
	cran = "symengine" 

	version("0.2.6", md5="c6f52b37cdddb4ef95dbcd8b7636bc3e")
	version("0.2.4", md5="248b8a9ece0f55a0e1951c11901b43bf")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("cmake", type=("build", "link", "run"))
	depends_on("gmp", type=("build", "link", "run"))
	depends_on("mpfr", type=("build", "link", "run"))
