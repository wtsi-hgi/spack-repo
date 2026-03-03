# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTt(RPackage):
	"""Display Tree Structured Data using Datatable Widget (DT)

	Wrapper of datatable widget, allowing display of data.tree objects.
            All arguments of the data.tree become columns and each node is a row.
            Adds column with buttons allowing folding and unfolding the levels.
	"""
	
	cran = "TT" 

	version("0.98", md5="f06cc9bb2c9db98ce693c5b747462f1c")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-data-tree", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
