# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAdaptalint(RPackage):
	"""Check Code Style Painlessly

	Infer the code style (which style rules are followed and which ones are 
    not) from one package and use it to check another. This makes it easier to
    find and correct the most important problems first.
	"""
	
	cran = "adaptalint" 

	version("0.2.4", md5="01cade9452855eb8bc301c8f8d24895a")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-lintr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
