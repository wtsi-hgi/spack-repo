# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLinne(RPackage):
	"""Convenient 'CSS'

	Conveniently generate 'CSS' using R code.
	"""
	
	homepage = "https://linne.john-coene.com/"
	cran = "linne" 

	version("0.0.2", md5="395befbe3a233825329c7e7c3ab1a52b")

	depends_on("r-r6", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
