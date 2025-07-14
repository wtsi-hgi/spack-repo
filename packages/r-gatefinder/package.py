# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGatefinder(RPackage):
	"""Projection-based Gating Strategy Optimization for Flow and Mass Cytometry

	Given a vector of cluster memberships for a cell population, identifies a sequence of gates (polygon filters on 2D scatter plots) for isolation of that cell type.
	"""
	
	bioc = "GateFinder"

	version("1.28.0", commit="a25389970e2f01892fe34ae95b65052ec01ee26d")
	version("1.22.0", commit="d87ec0d20377949c97479ce71107c27ff1af7d1e")

	depends_on("r-splancs", type=("build", "run"))
	depends_on("r-mvoutlier", type=("build", "run"))
	depends_on("r-diptest", type=("build", "run"))
	depends_on("r-flowcore", type=("build", "run"))
	depends_on("r-flowfp", type=("build", "run"))
