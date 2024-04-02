# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROndisc(RPackage):
	"""Fast, Universal, and Intuitive Computing on Large-Scale
Single-Cell Data

	Single-cell datasets are growing in size, posing challenges as well as opportunities for biology researchers. 'ondisc' (short for "on-disk single cell") enables users to easily and efficiently analyze large-scale single-cell data. 'ondisc' makes computing on large-scale single-cell data FUN: Fast, Universal, and iNtuitive.
	"""
	
	homepage = "https://timothy-barry.github.io/ondisc/"
	cran = "ondisc" 

	version("1.0.0", md5="fafbdc92fb33bcf3b2dfc0f4b205ca7b")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rhdf5", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rhdf5lib", type=("build", "run"))
	depends_on("zlib", type=("build", "link", "run"))
