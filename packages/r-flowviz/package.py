# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFlowviz(RPackage):
	"""Visualization for flow cytometry

	Provides visualization tools for flow cytometry data.
	"""
	
	bioc = "flowViz"

	version("1.72.0", commit="072bea418844fb6ff2a18c8bbe0befc305c23b31")
	version("1.66.0", commit="a2a15f661889c6c2122496c156a479c43811df63")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-flowcore", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-kernsmooth", type=("build", "run"))
	depends_on("r-latticeextra", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-hexbin", type=("build", "run"))
	depends_on("r-idpmisc", type=("build", "run"))
