# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RJqr(RPackage):
	"""Client for 'jq', a 'JSON' Processor

	Client for 'jq', a 'JSON' processor (<https://jqlang.github.io/jq/>), 
    written in C. 'jq' allows the following with 'JSON' data: index into, parse, 
    do calculations, cut up and filter, change key names and values, perform 
    conditionals and comparisons, and more.
	"""
	
	homepage = "https://docs.ropensci.org/jqr/"
	cran = "jqr" 

	version("1.3.3", md5="5ff27260cdc393fa0703f6d9c024d969")

	depends_on("r@3.1.2:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-lazyeval", type=("build", "run"))
	depends_on("jq", type=("build", "link", "run"))
