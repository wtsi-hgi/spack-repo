# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTidygapminder(RPackage):
	"""Easily Tidy Gapminder Datasets

	A toolset that allows you to easily import and tidy data sheets retrieved
    from Gapminder data web tools. It will therefore contribute to reduce the time
    used in data cleaning of Gapminder indicator data sheets as they are very messy.
	"""
	
	homepage = "https://ebedthan.github.io/tidygapminder"
	cran = "tidygapminder" 

	version("0.1.1", md5="173fb2bdd3b26871d748cdc3628b1625")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
