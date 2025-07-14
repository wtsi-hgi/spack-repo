# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSplinetimer(RPackage):
	"""Time-course differential gene expression data analysis using spline regression models followed by gene association network reconstruction

	This package provides functions for differential gene expression analysis of gene expression time-course data. Natural cubic spline regression models are used. Identified genes may further be used for pathway enrichment analysis and/or the reconstruction of time dependent gene regulatory association networks.
	"""
	
	bioc = "splineTimeR"

	version("1.36.0", commit="7f6e92c49b7845867b9c7a323ec87c5d70812ee3")
	version("1.30.0", commit="be96536a1875992ca8bdb8ffcbc57e811b084bc1")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-gseabase", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-genenet@1.2.13:", type=("build", "run"))
	depends_on("r-longitudinal@1.1.12:", type=("build", "run"))
	depends_on("r-fis", type=("build", "run"))
