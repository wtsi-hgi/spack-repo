# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgparty(RPackage):
	"""'ggplot' Visualizations for the 'partykit' Package

	Extends 'ggplot2' functionality to the 'partykit' package. 'ggparty' provides the necessary tools to create clearly structured and highly customizable visualizations for tree-objects of the class 'party'.
	"""
	
	homepage = "https://github.com/martin-borkovec/ggparty"
	cran = "ggparty" 

	version("1.0.0", md5="2b862a4e7f501e3ffc16110f78dce616")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-partykit", type=("build", "run"))
	depends_on("r-gtable", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
