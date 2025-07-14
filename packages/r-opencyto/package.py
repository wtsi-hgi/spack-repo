# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROpencyto(RPackage):
	"""Hierarchical Gating Pipeline for flow cytometry data

	This package is designed to facilitate the automated gating methods in sequential way to mimic the manual gating strategy.
	"""
	
	bioc = "openCyto"

	version("2.20.0", commit="6355a6622c77ecbca93411da2490ce16007d0336")
	version("2.14.0", commit="4b6c714c27cb6bd9053912d4acb5c417b75cea89")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-flowcore@1.99.17:", type=("build", "run"))
	depends_on("r-flowviz", type=("build", "run"))
	depends_on("r-ncdfflow@2.11.34:", type=("build", "run"))
	depends_on("r-flowworkspace@3.99.1:", type=("build", "run"))
	depends_on("r-flowclust@3.11.4:", type=("build", "run"))
	depends_on("r-rbgl", type=("build", "run"))
	depends_on("r-graph", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-cpp11", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
