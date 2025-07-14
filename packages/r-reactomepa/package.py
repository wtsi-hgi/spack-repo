# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RReactomepa(RPackage):
	"""Reactome Pathway Analysis

	This package provides functions for pathway analysis based on REACTOME pathway database. It implements enrichment analysis, gene set enrichment analysis and several functions for visualization.
	"""
	
	homepage = "https://yulab-smu.top/biomedical-knowledge-mining-book/"
	bioc = "ReactomePA"

	version("1.52.0", commit="00ffd9ac1f100f966cbd0a4b4b7f2f4354c743ba")
	version("1.46.0", commit="4fc270b4fcf88ce5791754fd97bf80aa4014fc7c")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-dose@3.5.1:", type=("build", "run"))
	depends_on("r-enrichplot", type=("build", "run"))
	depends_on("r-ggplot2@3.3.5:", type=("build", "run"))
	depends_on("r-ggraph", type=("build", "run"))
	depends_on("r-reactome-db", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-graphite", type=("build", "run"))
	depends_on("r-gson", type=("build", "run"))
