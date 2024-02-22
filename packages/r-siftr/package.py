# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSiftr(RPackage):
	"""Fuzzily Search a Dataframe to Find Relevant Columns

	Analysts who change projects frequently know that it can be hard
    to find the right column in an unfamiliar dataframe, especially when the
    dataframe spans hundreds of columns and millions of rows. 'siftr' is an
    interactive tool that finds relevant columns by fuzzily searching through
    a dataframe's column names, labels, factor levels, and unique values.
	"""
	
	homepage = "https://github.com/DesiQuintans/siftr"
	cran = "siftr" 

	version("1.1.0", md5="949f29bd0430d1417934744fcd946a6f")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-fastdigest", type=("build", "run"))
