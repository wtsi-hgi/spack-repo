# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTerm(RPackage):
	"""Create, Manipulate and Query Parameter Terms

	Creates, manipulates, queries and repairs vectors of
    parameter terms.  Parameter terms are the labels used to reference
    values in vectors, matrices and arrays. They represent the names in
    coefficient tables and the column names in 'mcmc' and 'mcmc.list'
    objects.
	"""
	
	homepage = "https://poissonconsulting.github.io/term/"
	cran = "term" 

	version("0.3.5", md5="78d310450c1590f5283baeafdea05d07")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-chk@0.8.1:", type=("build", "run"))
	depends_on("r-extras", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-universals", type=("build", "run"))
	depends_on("r-vctrs", type=("build", "run"))
