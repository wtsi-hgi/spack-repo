# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSparr(RPackage):
	"""Spatial and Spatiotemporal Relative Risk

	Provides functions to estimate kernel-smoothed spatial and spatio-temporal densities and relative risk functions, and perform subsequent inference. Methodological details can be found in the accompanying tutorial: Davies et al. (2018) <DOI:10.1002/sim.7577>.
	"""
	
	homepage = "https://tilmandavies.github.io/sparr/"
	cran = "sparr" 

	version("2.3-10", md5="c03965525a48fe35d67d633ef561a348")

	depends_on("r@2.10.1:", type=("build", "run"))
	depends_on("r-spatstat@2.3.0:", type=("build", "run"))
	depends_on("r-spatstat-utils", type=("build", "run"))
	depends_on("r-spatstat-geom", type=("build", "run"))
	depends_on("r-spatstat-explore", type=("build", "run"))
	depends_on("r-spatstat-random", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-misc3d", type=("build", "run"))
