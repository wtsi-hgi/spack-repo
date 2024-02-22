# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REditrules(RPackage):
	"""Parsing, Applying, and Manipulating Data Cleaning Rules

	Facilitates reading and manipulating (multivariate) data restrictions
    (edit rules) on numerical and categorical data. Rules can be defined with common R syntax
    and parsed to an internal (matrix-like format). Rules can be manipulated with
    variable elimination and value substitution methods, allowing for feasibility checks
    and more. Data can be tested against the rules and erroneous fields can be found based
    on Fellegi and Holt's generalized principle. Rules dependencies can be visualized with 
    using the 'igraph' package.
	"""
	
	homepage = "https://github.com/data-cleaning/editrules"
	cran = "editrules" 

	version("2.9.3", md5="cc1533a8e76f45cb7be394317f4a4616")

	depends_on("r@2.12:", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-lpsolveapi", type=("build", "run"))
