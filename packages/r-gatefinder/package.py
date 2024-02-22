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
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/GateFinder_1.22.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/GateFinder/GateFinder_1.22.0.tar.gz"]

	version("1.22.0", md5="4fcb13ba6ee293d3ffb30122b652df12")

	depends_on("r-splancs", type=("build", "run"))
	depends_on("r-mvoutlier", type=("build", "run"))
	depends_on("r-diptest", type=("build", "run"))
	depends_on("r-flowcore", type=("build", "run"))
	depends_on("r-flowfp", type=("build", "run"))
