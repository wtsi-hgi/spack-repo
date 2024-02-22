# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpreadr(RPackage):
	"""Simulating Spreading Activation in a Network

	The notion of spreading activation is a prevalent metaphor in the cognitive sciences. This package provides the tools for cognitive scientists and psychologists to conduct computer simulations that implement spreading activation in a network representation. The algorithmic method implemented in 'spreadr' subroutines follows the approach described in Vitevitch, Ercal, and Adagarla (2011, Frontiers), who viewed activation as a fixed cognitive resource that could spread among nodes that were connected to each other via edges or connections (i.e., a network). See Vitevitch, M. S., Ercal, G., & Adagarla, B. (2011). Simulating retrieval from a highly clustered network: Implications for spoken word recognition. Frontiers in Psychology, 2, 369. <doi:10.3389/fpsyg.2011.00369> and Siew, C. S. Q. (2019). spreadr: A R package to simulate spreading activation in a network. Behavior Research Methods, 51, 910-929. <doi: 10.3758/s13428-018-1186-5>.
	"""
	
	cran = "spreadr" 

	version("0.2.0", md5="95045af38149d55dda2d9168c5c1ad4e")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-extrafont", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
