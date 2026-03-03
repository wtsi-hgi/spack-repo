# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpatpomp(RPackage):
	"""Inference for Spatiotemporal Partially Observed Markov Processes

	Inference on panel data using spatiotemporal partially-observed Markov process (SpatPOMP) models. The 'spatPomp' package extends 'pomp' to include algorithms taking advantage of the spatial structure in order to assist with handling high dimensional processes. See Asfaw et al. (2023) <arXiv:2101.01157> for further description of the package.
	"""
	
	homepage = "https://github.com/kidusasfaw/spatPomp"
	cran = "spatPomp" 

	version("0.34.2", md5="734af646f0c1286ec7d3c1de1e77c861")

	depends_on("r-pomp", type=("build", "run"))
	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
