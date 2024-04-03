# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIvoTable(RPackage):
	"""Nicely Formatted Contingency Tables and Frequency Tables

	Nicely formatted frequency tables and contingency tables (1-way, 2-way, 3-way and 4-way tables), that can easily be exported to HTML or 'Office' documents. Designed to work with pipes.
	"""
	
	homepage = "https://github.com/mthulin/ivo.table"
	cran = "ivo.table" 

	version("0.4.1", md5="58027292a44570c4408f8df1f126fd5f")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-flextable", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-officer", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
