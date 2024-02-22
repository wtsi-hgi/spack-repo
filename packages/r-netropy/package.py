# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNetropy(RPackage):
	"""Statistical Entropy Analysis of Network Data

	Statistical entropy analysis of network data as introduced by Frank and Shafie (2016) <doi:10.1177/0759106315615511>, and in a forthcoming book by Nowicki, Shafie and Frank (2022).
	"""
	
	cran = "netropy" 

	version("0.1.0", md5="f88cc499547f5f02a58a2c41bfb742ca")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-ggraph", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
