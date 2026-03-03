# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPlnr(RPackage):
	"""A System for Planing Analyses

	A system to plan analyses within the mental model
    where you have one (or more) datasets and want to run either A) the same 
    function multiple times with different arguments, or B) multiple functions. 
    This is appropriate when you have multiple strata (e.g. locations, age groups)
    that you want to apply the same function to, or you have multiple variables 
    (e.g. exposures) that you want to apply the same statistical method to, or
    when you are creating the output for a report and you need multiple different
    tables or graphs.
	"""
	
	homepage = "https://www.csids.no/plnr/"
	cran = "plnr" 

	version("2022.11.23", md5="d6ecb3aced5b78e04b190cd80d2dafd3")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-uuid", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-fs", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-usethis", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
