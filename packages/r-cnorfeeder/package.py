# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCnorfeeder(RPackage):
	"""Integration of CellNOptR to add missing links

	This package integrates literature-constrained and data-driven methods to infer signalling networks from perturbation experiments. It permits to extends a given network with links derived from the data via various inference methods and uses information on physical interactions of proteins to guide and validate the integration of links.
	"""
	
	bioc = "CNORfeeder"

	version("1.48.0", commit="8b86d80191f8a72738b6b319c861db86a5d5b9bf")
	version("1.42.0", commit="6d3004ebcebd239bdb2139fb6f5da77b486290cd")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-cellnoptr@1.4:", type=("build", "run"))
	depends_on("r-graph", type=("build", "run"))
