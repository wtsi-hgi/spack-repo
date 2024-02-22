# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RR6p(RPackage):
	"""Design Patterns in R

	Build robust and maintainable software with object-oriented
    design patterns in R. Design patterns abstract and present in neat,
    well-defined components and interfaces the experience of many software
    designers and architects over many years of solving similar problems.
    These are solutions that have withstood the test of time with respect
    to re-usability, flexibility, and maintainability. 'R6P' provides
    abstract base classes with examples for a few known design patterns.
    The patterns were selected by their applicability to analytic projects
    in R. Using these patterns in R projects have proven effective in
    dealing with the complexity that data-driven applications possess.
	"""
	
	homepage = "https://tidylab.github.io/R6P/"
	cran = "R6P" 

	version("0.3.0", md5="4700d4fc492e9bf7a0f86e9ed5f1f50e")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-collections", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
