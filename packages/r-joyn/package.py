# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RJoyn(RPackage):
	"""Tool for Diagnosis of Tables Joins and Complementary Join
Features

	Tool for diagnosing table joins. It combines the speed of `collapse`
     and `data.table`, the flexibility of `dplyr`, and the diagnosis and features 
     of the `merge` command in `Stata`.
	"""
	
	homepage = "https://github.com/randrescastaneda/joyn"
	cran = "joyn" 

	version("0.2.0", md5="534d309f0cb8f2a47ebd3ddf5fb6fb73")
	version("0.1.4", md5="a19afd543bee21f7d158322320495e08")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-collapse@2.0.9:", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
