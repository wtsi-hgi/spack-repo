# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMetanetwork(RPackage):
	"""Handling and Representing Trophic Networks in Space and Time

	A toolbox to handle and represent trophic networks in space or time across aggregation levels. This package contains a layout algorithm specifically designed for trophic networks, using dimension reduction on a diffusion graph kernel and trophic levels. Importantly, this package provides a layout method applicable for large trophic networks.
	"""
	
	homepage = "https://github.com/MarcOhlmann/metanetwork"
	cran = "metanetwork" 

	version("0.7.0", md5="9c1e4b8d8554810cc466239e10f1e705")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggally", type=("build", "run"))
	depends_on("r-network", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-intergraph", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-visnetwork", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-ggimage", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-sna", type=("build", "run"))
