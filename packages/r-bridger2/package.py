# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBridger2(RPackage):
	"""Genome-Wide RNA Degradation Analysis Using BRIC-Seq Data

	BRIC-seq is a genome-wide approach for determining RNA stability in mammalian cells.
    This package provides a series of functions for performing quality check of your BRIC-seq data,
    calculation of RNA half-life for each transcript and comparison of RNA half-lives between two conditions.
	"""
	
	cran = "bridger2" 

	version("0.1.0", md5="15ec177d7164ae6d9327756d2f998b7d", url="https://cran.r-project.org/src/contrib/bridger2_0.1.0.tar.gz")

	depends_on("r@3.3.1:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinydashboard", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-bsda", type=("build", "run"))
	depends_on("r-outliers", type=("build", "run"))
