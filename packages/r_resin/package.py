# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RResin(RPackage):
	"""Response Item Networks ('ResIN')

	Contains various tools to perform and visualize Response Item Networks ('ResIN's'). 'ResIN' binarizes ordered-categorical and qualitative response choices from (survey) data, calculates pairwise associations and maps the location of each item response as a node in a force-directed network. Please refer to <https://www.resinmethod.net/> for more details.
	"""
	
	homepage = "https://github.com/pwarncke77/ResIN"
	cran = "ResIN" 

	version("1.1.0", md5="91a8da8ad6a5f30d494ac86fd16a58cf")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-ggplot2@3.4.2:", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-fastdummies@1.6.3:", type=("build", "run"))
	depends_on("r-qgraph@1.9.4:", type=("build", "run"))
	depends_on("r-igraph@1.4.2:", type=("build", "run"))
	depends_on("r-wcorr@1.9.6:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-directedclustering@0.1.1:", type=("build", "run"))
