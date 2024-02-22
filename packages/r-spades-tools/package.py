# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpadesTools(RPackage):
	"""Tools for Spatially Explicit Discrete Event Simulation (SpaDES) Models.

	Provides GIS and map utilities, plus additional modeling tools for
	developing cellular automata, dynamic raster models, and agent based models
	in 'SpaDES'.  Included are various methods for spatial spreading, spatial
	agents, GIS operations, random map generation, and others. See
	'?SpaDES.tools' for an categorized overview of these additional tools."""

	cran = "SpaDES.tools"

	maintainers("dorton21")

	version("2.0.5", md5="dc7c48f5bfff04fd8426ce5be39c9b30")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-backports", type=("build", "run"))
	depends_on("r-checkmate@1.8.2:", type=("build", "run"))
	depends_on("r-data-table@1.10.4:", type=("build", "run"))
	depends_on("r-fpcompare@0.2.1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-reproducible@2.0.9:", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
