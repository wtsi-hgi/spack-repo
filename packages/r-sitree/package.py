# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSitree(RPackage):
	"""Single Tree Simulator

	Framework to build an individual tree simulator.
	"""
	
	cran = "sitree" 

	version("0.1-14", md5="31761654821fc7b86762880e4ed4f36a")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
