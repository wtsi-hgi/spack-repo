# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPipefittr(RPackage):
	"""Convert Nested Functions to Pipes

	To take nested function calls and convert them to a more readable form using pipes from package 'magrittr'.
	"""
	
	cran = "pipefittr" 

	version("0.1.2", md5="b6f361535481c10bdd9b25a46f6063a4")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-miniui@0.1.1:", type=("build", "run"))
	depends_on("r-rstudioapi@0.4:", type=("build", "run"))
	depends_on("r-shiny@0.13:", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
